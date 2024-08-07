"""added models and generate qrcode

Revision ID: aab55bef4222
Revises: 
Create Date: 2024-07-08 19:44:39.771655

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'aab55bef4222'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('qr_code',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('MerchantName', sa.String(length=300), nullable=False),
    sa.Column('RefNo', sa.String(length=100), nullable=False),
    sa.Column('Amount', sa.String(length=100), nullable=False),
    sa.Column('TrxCode', sa.String(length=100), nullable=False),
    sa.Column('CPI', sa.String(length=100), nullable=False),
    sa.Column('Size', sa.String(length=100), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('qr_code')
    # ### end Alembic commands ###
