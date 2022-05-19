"""add usee_details table

Revision ID: e0a4c4f2b247
Revises: e4c2fac7ba5b
Create Date: 2022-05-19 12:36:31.449424

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e0a4c4f2b247'
down_revision = 'e4c2fac7ba5b'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'img_file')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('img_file', sa.VARCHAR(length=130), nullable=True))
    # ### end Alembic commands ###