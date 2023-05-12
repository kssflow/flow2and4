"""empty message

Revision ID: 9e97a9949846
Revises: 474fc898387b
Create Date: 2023-05-11 11:19:44.001028

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '9e97a9949846'
down_revision = '474fc898387b'
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
    op.create_table('user_backdrop',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.String(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('url', sa.String(), nullable=False),
    sa.Column('filename', sa.String(), nullable=False),
    sa.Column('original_filename', sa.String(), nullable=False),
    sa.Column('mimetype', sa.String(), nullable=True),
    sa.Column('filesize', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], name=op.f('fk_user_backdrop_user_id_user')),
    sa.PrimaryKeyConstraint('id', name=op.f('pk_user_backdrop'))
    )
    # ### end Alembic commands ###


def downgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('user_backdrop')
    # ### end Alembic commands ###


def upgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###

