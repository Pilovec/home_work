"""delete language to posts

Revision ID: e460fa4f866f
Revises: cd8bccefb0b2
Create Date: 2019-06-11 09:42:17.317435

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e460fa4f866f'
down_revision = 'cd8bccefb0b2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('post', 'language')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('post', sa.Column('language', sa.VARCHAR(length=5), nullable=True))
    # ### end Alembic commands ###
