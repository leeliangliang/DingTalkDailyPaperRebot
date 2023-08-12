"""clash migration.

Revision ID: e92529d29e95
Revises: 390f96b83b64
Create Date: 2023-08-12 17:36:48.010965

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e92529d29e95'
down_revision = '390f96b83b64'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('clash_subscribe',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', sa.String(length=120), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('clash_subscribe')
    # ### end Alembic commands ###