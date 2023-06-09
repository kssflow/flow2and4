from flask import Flask, request, make_response, url_for, g
from urllib.parse import urlparse
from http import HTTPStatus
from flask_login import LoginManager
from sqlalchemy import MetaData
from celery import Celery, Task

login_manager = LoginManager()


def create_app(mode: str = "dev"):
    """Create flask application."""

    app = Flask(__name__, subdomain_matching=True)

    from flow2and4.config import WebConfig

    app.config.from_object(WebConfig())

    if mode == "dev":
        app.config["SERVER_NAME"] = "localhost:5000"

    if mode == "test":
        from flow2and4.config import WebTestConfig

        app.config.from_object(WebTestConfig())

    if mode == "prodlike":
        from flow2and4.config import WebProdConfig
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.config.from_object(WebProdConfig())
        app.config["SERVER_NAME"] = "localhost"
        # Tell Flask it is Behind a Proxy
        # https://flask.palletsprojects.com/en/2.3.x/deploying/proxy_fix/
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    if mode == "prod":
        from flow2and4.config import WebProdConfig
        from werkzeug.middleware.proxy_fix import ProxyFix

        app.config.from_object(WebProdConfig())
        app.config["SERVER_NAME"] = "flow2and4.me"
        # Tell Flask it is Behind a Proxy
        # https://flask.palletsprojects.com/en/2.3.x/deploying/proxy_fix/
        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_proto=1, x_host=1, x_prefix=1)

    # [START] Register extensions
    from flask_wtf import CSRFProtect
    from flow2and4.database import db, migrate

    # Celery.
    celery_init_app(app)

    # CSRF protection.
    csrf = CSRFProtect()
    csrf.init_app(app)

    # Database.
    db.init_app(app)
    migrate.init_app(app, db)

    # Database____sqlite specific foreign key enabled.
    def _fk_pragma_on_connect(dbapi_con, con_record):  # noqa
        dbapi_con.execute("PRAGMA foreign_keys=ON")

    with app.app_context():
        from sqlalchemy import event

        for _engine in db.engines.values():
            event.listen(_engine, "connect", _fk_pragma_on_connect)

    # Bcrypt.
    from flask_bcrypt import Bcrypt

    bcrypt = Bcrypt()
    bcrypt.init_app(app)

    # Login.
    from flow2and4.csduck.auth.service import get_user_for_session
    from flow2and4.pyduck.auth.service import get_pyduck_user_for_session

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        if "pyduck" in urlparse(request.root_url).netloc:
            return get_pyduck_user_for_session(id=int(user_id))

        return get_user_for_session(id=int(user_id))

    # Customize the login process.
    @login_manager.unauthorized_handler
    def unauthorized():
        # TODO: This is not safe.
        next_ = request.referrer if request.referrer else None

        res = make_response()
        res.headers["HX-Reswap"] = "none"
        res.headers["HX-Trigger"] = "login-required"
        return res

    # Register extensions [END]

    # [START] Register blueprints
    from flow2and4.csduck.views import bp as bp
    from flow2and4.myweb.views import bp as bp_rodi
    from flow2and4.faduck.views import bp as bp_faduck
    from flow2and4.pyduck.views import bp as bp_pyduck

    app.register_blueprint(bp_rodi)
    app.register_blueprint(bp, subdomain="csduck")
    app.register_blueprint(bp_faduck, subdomain="faduck")
    app.register_blueprint(bp_pyduck, subdomain="pyduck")

    # Register blueprints [END]

    return app


def celery_init_app(app: Flask) -> Celery:
    """Configure celery app and return celery app."""

    class FlaskTask(Task):
        """Celery Task with flask application context."""

        def __call__(self, *args, **kwargs):
            with app.app_context():
                return self.run(*args, **kwargs)

    celery_app = Celery(app.name, task_cls=FlaskTask)
    celery_app.config_from_object(app.config["CELERY"])
    celery_app.set_default()
    app.extensions["celery"] = celery_app
    return celery_app
