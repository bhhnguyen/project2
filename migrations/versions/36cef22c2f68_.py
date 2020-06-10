"""empty message

Revision ID: 36cef22c2f68
Revises: 
Create Date: 2020-06-09 20:50:22.018917

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '36cef22c2f68'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('US_Presidents_data')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('US_Presidents_data',
    sa.Column('rowid', sa.INTEGER(), server_default=sa.text('nextval(\'"US_Presidents_data_rowid_seq"\'::regclass)'), nullable=False),
    sa.Column('year', sa.CHAR(length=6), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('party', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('candidate', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('writein', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.Column('candidatevotes', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('totalvotes', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###
