"""empty message

Revision ID: af3cbb30b559
Revises: b35af1ed91c6
Create Date: 2022-08-11 16:37:52.349591

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'af3cbb30b559'
down_revision = 'b35af1ed91c6'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('person', sa.Column('username', sa.String(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('person', 'username')
    # ### end Alembic commands ###
