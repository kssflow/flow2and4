"""empty message

Revision ID: 116a148da1ae
Revises: dd2e7c83b99b
Create Date: 2023-05-17 10:19:57.477222

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '116a148da1ae'
down_revision = 'dd2e7c83b99b'
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
    with op.batch_alter_table('user_action', schema=None) as batch_op:
        batch_op.add_column(sa.Column('target_id', sa.Integer(), nullable=True))
        batch_op.drop_index('ix_user_action_action_target_type')
        batch_op.drop_index('ix_user_action_user_id_user_action_action_type_user_action_action_target_type')
        batch_op.drop_constraint('uq_user_action_user_id_action_type_action_target_type_action_target_id', type_='unique')
        batch_op.create_index(batch_op.f('ix_user_action_user_id_user_action_action_type_user_action_target_id'), ['user_id', 'action_type', 'target_id'], unique=False)
        batch_op.create_unique_constraint(batch_op.f('uq_user_action_user_id_action_type_target_id'), ['user_id', 'action_type', 'target_id'])
        batch_op.drop_column('action_target_id')
        batch_op.drop_column('action_target_type')

    # ### end Alembic commands ###


def downgrade_pyduck():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('user_action', schema=None) as batch_op:
        batch_op.add_column(sa.Column('action_target_type', sa.VARCHAR(), nullable=True))
        batch_op.add_column(sa.Column('action_target_id', sa.INTEGER(), nullable=True))
        batch_op.drop_constraint(batch_op.f('uq_user_action_user_id_action_type_target_id'), type_='unique')
        batch_op.drop_index(batch_op.f('ix_user_action_user_id_user_action_action_type_user_action_target_id'))
        batch_op.create_unique_constraint('uq_user_action_user_id_action_type_action_target_type_action_target_id', ['user_id', 'action_type', 'action_target_type', 'action_target_id'])
        batch_op.create_index('ix_user_action_user_id_user_action_action_type_user_action_action_target_type', ['user_id', 'action_type', 'action_target_type'], unique=False)
        batch_op.create_index('ix_user_action_action_target_type', ['action_target_type'], unique=False)
        batch_op.drop_column('target_id')

    # ### end Alembic commands ###


def upgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade_faduck():
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###
