"""create fundData  table

Revision ID: 2120ae76a5ee
Revises: 1a245b65cbc8
Create Date: 2022-07-20 17:43:42.988764

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '2120ae76a5ee'
down_revision = '1a245b65cbc8'
branch_labels = None
depends_on = None


def upgrade() -> None:
            op.create_table('fundData',
                    sa.Column('id', sa.Integer(), nullable=False),
                    sa.Column('Api', sa.Integer(), nullable=False),
                    sa.Column('Nombre_Fondo', sa.String(), nullable=False),
                    sa.Column('Fecha', sa.String(), nullable=False),
                    sa.Column('date', sa.TIMESTAMP(timezone=True), nullable=False, 
                                            server_default=sa.text('NOW()')),
                    sa.PrimaryKeyConstraint('id')
                    )


def downgrade() -> None:
        op.drop_column('fundData', 'date')
        op.drop_column('fundData', 'Fecha')
        op.drop_column('fundData', 'Nombre_Fondo')
        op.drop_column('fundData', 'Api')
        op.drop_column('fundData', 'id')
