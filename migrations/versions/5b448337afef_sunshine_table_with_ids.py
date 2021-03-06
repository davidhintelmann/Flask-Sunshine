"""sunshine table with ids

Revision ID: 5b448337afef
Revises: 48b9811f3205
Create Date: 2020-11-02 12:08:46.128152

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '5b448337afef'
down_revision = '48b9811f3205'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sunshine', sa.Column('year', sa.Integer(), nullable=True))
    op.create_index(op.f('ix_sunshine_first_name'), 'sunshine', ['first_name'], unique=False)
    op.create_index(op.f('ix_sunshine_last_name'), 'sunshine', ['last_name'], unique=False)
    op.create_index(op.f('ix_sunshine_salary'), 'sunshine', ['salary'], unique=False)
    op.create_index(op.f('ix_sunshine_sector'), 'sunshine', ['sector'], unique=False)
    op.create_index(op.f('ix_sunshine_taxable'), 'sunshine', ['taxable'], unique=False)
    op.create_index(op.f('ix_sunshine_year'), 'sunshine', ['year'], unique=False)
    op.drop_column('sunshine', 'calendar_year')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sunshine', sa.Column('calendar_year', sa.BIGINT(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_sunshine_year'), table_name='sunshine')
    op.drop_index(op.f('ix_sunshine_taxable'), table_name='sunshine')
    op.drop_index(op.f('ix_sunshine_sector'), table_name='sunshine')
    op.drop_index(op.f('ix_sunshine_salary'), table_name='sunshine')
    op.drop_index(op.f('ix_sunshine_last_name'), table_name='sunshine')
    op.drop_index(op.f('ix_sunshine_first_name'), table_name='sunshine')
    op.drop_column('sunshine', 'year')
    # ### end Alembic commands ###
