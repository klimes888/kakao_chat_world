"""add content data

Revision ID: 83f190527c28
Revises: 0d2f6848360f
Create Date: 2024-05-27 14:34:47.436495

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '83f190527c28'
down_revision = '0d2f6848360f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('force_defense', schema=None) as batch_op:
        batch_op.alter_column('desc',
               existing_type=sa.VARCHAR(length=150),
               type_=sa.String(length=300),
               existing_nullable=False)

    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('count', sa.String(length=12), nullable=False))
        batch_op.drop_column('weapon_type')
        batch_op.drop_column('value')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('weapon', schema=None) as batch_op:
        batch_op.add_column(sa.Column('value', postgresql.JSON(astext_type=sa.Text()), autoincrement=False, nullable=False))
        batch_op.add_column(sa.Column('weapon_type', sa.VARCHAR(length=40), autoincrement=False, nullable=False))
        batch_op.drop_column('count')

    with op.batch_alter_table('force_defense', schema=None) as batch_op:
        batch_op.alter_column('desc',
               existing_type=sa.String(length=300),
               type_=sa.VARCHAR(length=150),
               existing_nullable=False)

    # ### end Alembic commands ###
