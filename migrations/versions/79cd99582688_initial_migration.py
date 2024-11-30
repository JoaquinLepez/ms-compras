"""initial migration

Revision ID: 79cd99582688
Revises: 
Create Date: 2024-11-30 17:08:10.079082

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '79cd99582688'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('compras',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('producto_id', sa.Integer(), nullable=False),
    sa.Column('fecha_compra', sa.DateTime(), nullable=False),
    sa.Column('direccion_envio', sa.String(length=80), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    schema='compras'
    )
    op.drop_table('alembic_version')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('alembic_version',
    sa.Column('version_num', sa.VARCHAR(length=32), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('version_num', name='alembic_version_pkc')
    )
    op.drop_table('compras', schema='compras')
    # ### end Alembic commands ###