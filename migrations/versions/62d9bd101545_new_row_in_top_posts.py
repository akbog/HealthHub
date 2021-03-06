"""new row in top_posts

Revision ID: 62d9bd101545
Revises: 6b07301ec234
Create Date: 2019-12-07 19:38:13.090620

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '62d9bd101545'
down_revision = '6b07301ec234'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('top_posts',
    sa.Column('post_id', sa.Integer(), nullable=False),
    sa.Column('forum_id', sa.Integer(), nullable=False),
    sa.Column('forum_name', sa.String(length=128), nullable=False),
    sa.ForeignKeyConstraint(['forum_id'], ['post.forum_id'], ),
    sa.ForeignKeyConstraint(['forum_name'], ['forum.forum_name'], ),
    sa.ForeignKeyConstraint(['post_id'], ['post.post_id'], ),
    sa.PrimaryKeyConstraint('post_id', 'forum_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('top_posts')
    # ### end Alembic commands ###
