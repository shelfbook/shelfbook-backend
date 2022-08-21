"""Test 5

Revision ID: 4a01671f1406
Revises: 9cbd7350a619
Create Date: 2022-08-21 13:30:25.295759

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4a01671f1406'
down_revision = '9cbd7350a619'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('authors', sa.Column('is_confirmed', sa.Boolean(), server_default='false', nullable=True))
    op.add_column('authors', sa.Column('is_processed', sa.Boolean(), server_default='false', nullable=True))
    op.add_column('authors', sa.Column('created_at', sa.DateTime(), nullable=True))
    op.add_column('authors', sa.Column('updated_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('authors', 'updated_at')
    op.drop_column('authors', 'created_at')
    op.drop_column('authors', 'is_processed')
    op.drop_column('authors', 'is_confirmed')
    # ### end Alembic commands ###
