"""empty message

Revision ID: 839e32eca7ff
Revises: 83f190527c28
Create Date: 2024-05-29 14:46:10.749889

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '839e32eca7ff'
down_revision = '83f190527c28'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignment', schema=None) as batch_op:
        batch_op.add_column(sa.Column('world_id', sa.Integer(), nullable=True))
        batch_op.add_column(sa.Column('content_id', sa.Integer(), nullable=True))
        batch_op.alter_column('sub_content_id',
               existing_type=sa.INTEGER(),
               nullable=True)
        batch_op.create_foreign_key(None, 'content', ['content_id'], ['id'])
        batch_op.create_foreign_key(None, 'world', ['world_id'], ['id'])

    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.add_column(sa.Column('world_id', sa.Integer(), nullable=False))
        batch_op.alter_column('desc',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=300),
               existing_nullable=False)
        batch_op.create_foreign_key(None, 'world', ['world_id'], ['id'])

    with op.batch_alter_table('world', schema=None) as batch_op:
        batch_op.add_column(sa.Column('bot_id', sa.String(length=120), nullable=False))
        batch_op.create_unique_constraint(None, ['bot_id'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('world', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')
        batch_op.drop_column('bot_id')

    with op.batch_alter_table('content', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('desc',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)
        batch_op.drop_column('world_id')

    with op.batch_alter_table('assignment', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.drop_constraint(None, type_='foreignkey')
        batch_op.alter_column('sub_content_id',
               existing_type=sa.INTEGER(),
               nullable=False)
        batch_op.drop_column('content_id')
        batch_op.drop_column('world_id')

    # ### end Alembic commands ###
