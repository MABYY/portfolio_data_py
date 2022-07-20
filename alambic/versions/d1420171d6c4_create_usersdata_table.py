"""create usersData  table

Revision ID: d1420171d6c4
Revises: 
Create Date: 2022-07-20 17:02:20.774401

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd1420171d6c4'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
        op.create_table('usersData',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('username', sa.String(), nullable=False),
                    sa.Column('email', sa.String(), nullable=False),
                    sa.Column('password', sa.String(), nullable=False),
                    sa.Column('role', sa.String(), server_default='user', 
                    nullable=False),
                    sa.PrimaryKeyConstraint('id')
                    )



def downgrade() -> None:
    op.drop_column('usersData', 'role')
    op.drop_column('usersData', 'password')
    op.drop_column('usersData', 'email')
    op.drop_column('usersData', 'username')
    op.drop_column('usersData', 'id')
