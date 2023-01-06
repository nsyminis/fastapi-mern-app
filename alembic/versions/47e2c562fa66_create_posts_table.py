"""create posts table

Revision ID: 47e2c562fa66
Revises: 
Create Date: 2023-01-06 15:27:53.764927

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '47e2c562fa66'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    op.create_table('posts', sa.Column('id', sa.Integer(), nullable=False, primary_key=True), sa.Column('title', sa.String(), nullable=False))
    pass


def downgrade():
    op.drop_table('posts')
    pass
