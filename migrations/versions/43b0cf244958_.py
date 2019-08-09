"""empty message

Revision ID: 43b0cf244958
Revises: dc256e640729
Create Date: 2019-08-09 16:22:34.409057

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '43b0cf244958'
down_revision = 'dc256e640729'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shoping_cart',
    sa.Column('users_id', sa.Integer(), nullable=False),
    sa.Column('products_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], ),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('users_id', 'products_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shoping_cart')
    # ### end Alembic commands ###
