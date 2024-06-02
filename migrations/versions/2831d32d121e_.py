"""empty message

Revision ID: 2831d32d121e
Revises: 61c8941d8a95
Create Date: 2024-06-02 07:31:05.201879

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2831d32d121e'
down_revision = '61c8941d8a95'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignment', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.VARCHAR(length=50),
               type_=sa.SmallInteger(),
               existing_nullable=False)

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('assignment', schema=None) as batch_op:
        batch_op.alter_column('role',
               existing_type=sa.SmallInteger(),
               type_=sa.VARCHAR(length=50),
               existing_nullable=False)

    # ### end Alembic commands ###
