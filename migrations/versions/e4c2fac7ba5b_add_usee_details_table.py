"""add usee_details table

Revision ID: e4c2fac7ba5b
Revises: ca0467615614
Create Date: 2022-05-19 12:35:17.308792

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e4c2fac7ba5b'
down_revision = 'ca0467615614'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_details',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('classes', sa.String(), nullable=True),
    sa.Column('package', sa.String(), nullable=True),
    sa.Column('trainer', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.drop_column('user', 'classes')
    op.drop_column('user', 'trainer')
    op.drop_column('user', 'package')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('package', sa.VARCHAR(), nullable=True))
    op.add_column('user', sa.Column('trainer', sa.VARCHAR(), nullable=True))
    op.add_column('user', sa.Column('classes', sa.VARCHAR(), nullable=True))
    op.drop_table('user_details')
    # ### end Alembic commands ###