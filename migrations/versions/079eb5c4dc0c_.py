"""empty message

Revision ID: 079eb5c4dc0c
Revises: 2831d32d121e
Create Date: 2024-06-02 07:56:13.711644

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '079eb5c4dc0c'
down_revision = '2831d32d121e'
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
