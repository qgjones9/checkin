"""populating table

Revision ID: c8690960223e
Revises: 
Create Date: 2019-10-16 19:11:13.259563

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c8690960223e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('teacher',
    sa.Column('grade_level', sa.String(length=2), nullable=False),
    sa.Column('teacher_id', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('grade_level')
    )
    op.create_table('child',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('first_name', sa.String(length=64), nullable=False),
    sa.Column('last_name', sa.String(length=64), nullable=True),
    sa.Column('grade_level', sa.String(length=2), nullable=True),
    sa.ForeignKeyConstraint(['grade_level'], ['teacher.grade_level'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_child_first_name'), 'child', ['first_name'], unique=True)
    op.create_index(op.f('ix_child_last_name'), 'child', ['last_name'], unique=True)
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('faculty', sa.Boolean(), nullable=False),
    sa.Column('admin', sa.Boolean(), nullable=False),
    sa.Column('child_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['child_id'], ['child.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_username'), 'user', ['username'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_username'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    op.drop_index(op.f('ix_child_last_name'), table_name='child')
    op.drop_index(op.f('ix_child_first_name'), table_name='child')
    op.drop_table('child')
    op.drop_table('teacher')
    # ### end Alembic commands ###
