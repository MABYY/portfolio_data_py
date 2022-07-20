"""add created_at table to  usersData  table

Revision ID: 1a245b65cbc8
Revises: d1420171d6c4
Create Date: 2022-07-20 17:32:15.774595

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1a245b65cbc8'
down_revision = 'd1420171d6c4'
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.add_column('usersData', sa.Column(
        'created_at', sa.TIMESTAMP(timezone=True), nullable=False, server_default=sa.text('NOW()')))


def downgrade() -> None:
     op.drop_column('usersData', 'created_at')

