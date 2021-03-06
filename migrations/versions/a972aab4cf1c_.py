"""empty message

Revision ID: a972aab4cf1c
Revises: 
Create Date: 2018-08-30 10:51:40.020976

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a972aab4cf1c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('changes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('desc', sa.String(length=100), nullable=True),
    sa.Column('model', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('group',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.Column('boss_id', sa.Integer(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=50), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('title',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('add_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('translation',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('title_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.ForeignKeyConstraint(['title_id'], ['title.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100, collation='NOCASE'), server_default='', nullable=False),
    sa.Column('password_hash', sa.String(), nullable=True),
    sa.Column('about', sa.String(length=250), nullable=True),
    sa.Column('group_id', sa.Integer(), nullable=True),
    sa.Column('avatar', sa.String(), nullable=True),
    sa.ForeignKeyConstraint(['group_id'], ['group.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('chapter',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('add_date', sa.DateTime(), nullable=True),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('img', sa.String(), nullable=True),
    sa.Column('uploader_id', sa.Integer(), nullable=True),
    sa.Column('translation_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['translation_id'], ['translation.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('roles',
    sa.Column('role_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('role_id', 'user_id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('roles')
    op.drop_table('chapter')
    op.drop_table('user')
    op.drop_table('translation')
    op.drop_table('title')
    op.drop_table('role')
    op.drop_table('group')
    op.drop_table('changes')
    # ### end Alembic commands ###
