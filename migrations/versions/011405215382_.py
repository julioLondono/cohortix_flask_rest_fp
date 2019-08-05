"""empty message

Revision ID: 011405215382
Revises: 71b4b9da0a4d
Create Date: 2019-08-03 21:57:30.809170

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import mysql

# revision identifiers, used by Alembic.
revision = '011405215382'
down_revision = '71b4b9da0a4d'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('person_id', sa.Integer(), nullable=False))
    op.drop_constraint('address_ibfk_1', 'address', type_='foreignkey')
    op.create_foreign_key(None, 'address', 'user', ['person_id'], ['id'])
    op.drop_column('address', 'personid')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('address', sa.Column('personid', mysql.INTEGER(display_width=11), autoincrement=False, nullable=False))
    op.drop_constraint(None, 'address', type_='foreignkey')
    op.create_foreign_key('address_ibfk_1', 'address', 'user', ['personid'], ['id'])
    op.drop_column('address', 'person_id')
    # ### end Alembic commands ###
