"""empty message

Revision ID: ba2afc95e559
Revises: e4873433fa3a
Create Date: 2019-08-03 21:06:38.433760

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = 'ba2afc95e559'
down_revision = 'e4873433fa3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('userLastName', sa.String(length=45), nullable=False))
    op.drop_column('user', 'user_lastName')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('user_lastName', mysql.VARCHAR(length=45), nullable=False))
    op.drop_column('user', 'userLastName')
    # ### end Alembic commands ###
