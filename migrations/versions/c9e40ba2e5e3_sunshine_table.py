"""sunshine table

Revision ID: c9e40ba2e5e3
Revises: cf497c66e438
Create Date: 2020-10-30 06:48:54.481111

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c9e40ba2e5e3'
down_revision = 'cf497c66e438'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('sunshine')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('sunshine',
    sa.Column('sector', sa.VARCHAR(length=56), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(length=26), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(length=25), autoincrement=False, nullable=True),
    sa.Column('salary', sa.NUMERIC(precision=12, scale=2), autoincrement=False, nullable=True),
    sa.Column('taxable', sa.NUMERIC(precision=11, scale=2), autoincrement=False, nullable=True),
    sa.Column('employer', sa.VARCHAR(length=193), autoincrement=False, nullable=True),
    sa.Column('job_title', sa.VARCHAR(length=300), autoincrement=False, nullable=True),
    sa.Column('calendar_year', sa.BIGINT(), autoincrement=False, nullable=True)
    )
    # ### end Alembic commands ###