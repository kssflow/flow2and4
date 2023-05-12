"""empty message

Revision ID: 1fbaabc538bf
Revises: 9e97a9949846
Create Date: 2023-05-11 17:35:18.121763

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1fbaabc538bf'
down_revision = '9e97a9949846'
branch_labels = None
depends_on = None


def upgrade(engine_name):
    globals()["upgrade_%s" % engine_name]()


def downgrade(engine_name):
    globals()["downgrade_%s" % engine_name]()





def upgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def upgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_sns',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('platform', sa.String(), nullable=False),
    sa.Column('link', sa.String(), nullable=False),
    sa.Column('public', sa.Boolean(), nullable=False),
    sa.Column('created_at', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_sns_user_id_user'), ondelete="CASCADE'"),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_sns'))
    )
    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.add_column(sa.Column('about_me', sa.String(), nullable=True))

    with op.batch_alter_table('user_avatar', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_avatar_user_id'), ['user_id'])
        batch_op.drop_constraint('fk_user_avatar_user_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_user_avatar_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user_backdrop', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_backdrop_user_id'), ['user_id'])
        batch_op.drop_constraint('fk_user_backdrop_user_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_user_backdrop_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    with op.batch_alter_table('user_verification_email', schema=None) as batch_op:
        batch_op.create_unique_constraint(batch_op.f('uq_user_verification_email_user_id'), ['user_id'])
        batch_op.drop_constraint('fk_user_verification_email_user_id_user', type_='foreignkey')
        batch_op.create_foreign_key(batch_op.f('fk_user_verification_email_user_id_user'), 'user', ['user_id'], ['id'], ondelete='CASCADE')

    # ### end Alembic commands ###


def downgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_verification_email', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_verification_email_user_id_user'), type_='foreignkey')
        batch_op.create_foreign_key('fk_user_verification_email_user_id_user', 'user', ['user_id'], ['id'])
        batch_op.drop_constraint(batch_op.f('uq_user_verification_email_user_id'), type_='unique')

    with op.batch_alter_table('user_backdrop', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_backdrop_user_id_user'), type_='foreignkey')
        batch_op.create_foreign_key('fk_user_backdrop_user_id_user', 'user', ['user_id'], ['id'])
        batch_op.drop_constraint(batch_op.f('uq_user_backdrop_user_id'), type_='unique')

    with op.batch_alter_table('user_avatar', schema=None) as batch_op:
        batch_op.drop_constraint(batch_op.f('fk_user_avatar_user_id_user'), type_='foreignkey')
        batch_op.create_foreign_key('fk_user_avatar_user_id_user', 'user', ['user_id'], ['id'])
        batch_op.drop_constraint(batch_op.f('uq_user_avatar_user_id'), type_='unique')

    with op.batch_alter_table('user', schema=None) as batch_op:
        batch_op.drop_column('about_me')

    op.drop_table('user_sns')
    # ### end Alembic commands ###


def upgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

