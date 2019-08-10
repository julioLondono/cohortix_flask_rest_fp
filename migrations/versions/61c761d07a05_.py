"""empty message

Revision ID: 61c761d07a05
Revises: 6e570913eba3
Create Date: 2019-08-10 16:10:13.608465

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '61c761d07a05'
down_revision = '6e570913eba3'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('shopingcart')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('shopingcart',
    sa.Column('users_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.Column('products_id', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['products_id'], ['products.id'], name='shopingcart_ibfk_1'),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], name='shopingcart_ibfk_2'),
    sa.PrimaryKeyConstraint('users_id', 'products_id'),
    mysql_default_charset='latin1',
    mysql_engine='InnoDB'
    )
    # ### end Alembic commands ###