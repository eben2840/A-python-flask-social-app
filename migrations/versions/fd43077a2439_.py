"""empty message

Revision ID: fd43077a2439
Revises: 8d33bc8fb537
Create Date: 2022-09-29 12:04:35.088630

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fd43077a2439'
down_revision = '8d33bc8fb537'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('school', sa.String(length=20), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'school')
    # ### end Alembic commands ###
