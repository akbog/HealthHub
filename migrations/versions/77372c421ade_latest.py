"""latest

Revision ID: 77372c421ade
Revises: 6f0733fd3d88
Create Date: 2019-10-25 14:44:47.220144

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '77372c421ade'
down_revision = '6f0733fd3d88'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('confirmed', sa.Boolean(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'confirmed')
    # ### end Alembic commands ###