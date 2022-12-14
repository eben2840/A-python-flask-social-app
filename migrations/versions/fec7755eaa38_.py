"""empty message

Revision ID: fec7755eaa38
Revises: 2868d00e94ff
Create Date: 2022-09-14 16:37:11.856349

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'fec7755eaa38'
down_revision = '2868d00e94ff'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('person',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=200), nullable=True),
    sa.Column('yearCompleted', sa.String(length=200), nullable=True),
    sa.Column('nationality', sa.String(length=200), nullable=True),
    sa.Column('contact', sa.Integer(), nullable=True),
    sa.Column('faculty', sa.String(length=200), nullable=True),
    sa.Column('hallofresidence', sa.String(length=200), nullable=True),
    sa.Column('password', sa.String(length=20), nullable=True),
    sa.Column('email', sa.String(length=20), nullable=True),
    sa.Column('phone', sa.String(length=10), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('contact'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('faculty'),
    sa.UniqueConstraint('hallofresidence'),
    sa.UniqueConstraint('name'),
    sa.UniqueConstraint('nationality'),
    sa.UniqueConstraint('password'),
    sa.UniqueConstraint('phone'),
    sa.UniqueConstraint('yearCompleted')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('person')
    # ### end Alembic commands ###
