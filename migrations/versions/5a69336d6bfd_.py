"""empty message

Revision ID: 5a69336d6bfd
Revises: 9001f8f78ecf
Create Date: 2022-09-19 22:03:09.897716

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5a69336d6bfd'
down_revision = '9001f8f78ecf'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('indexnumber', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'indexnumber')
    # ### end Alembic commands ###