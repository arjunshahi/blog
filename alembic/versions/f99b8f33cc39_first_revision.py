"""first revision

Revision ID: f99b8f33cc39
Revises: 
Create Date: 2023-01-05 18:10:34.246760

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'f99b8f33cc39'
down_revision = None
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('full_name', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=True),
    sa.Column('is_superuser', sa.Boolean(), nullable=True),
    sa.Column('joined_on', sa.TIMESTAMP(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_user_email'), 'user', ['email'], unique=True)
    op.create_index(op.f('ix_user_id'), 'user', ['id'], unique=False)
    op.create_table('blog',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=200), nullable=False),
    sa.Column('content', sa.Text(), nullable=False),
    sa.Column('is_published', sa.Boolean(), nullable=True),
    sa.Column('posted_on', sa.TIMESTAMP(), nullable=True),
    sa.Column('posted_by_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['posted_by_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blog_id'), 'blog', ['id'], unique=False)
    op.create_index(op.f('ix_blog_posted_by_id'), 'blog', ['posted_by_id'], unique=False)
    op.create_table('blogcomment',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('comment', sa.String(length=255), nullable=False),
    sa.Column('blog_id', sa.Integer(), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['blog_id'], ['blog.id'], ),
    sa.ForeignKeyConstraint(['user_id'], ['user.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_blogcomment_blog_id'), 'blogcomment', ['blog_id'], unique=False)
    op.create_index(op.f('ix_blogcomment_id'), 'blogcomment', ['id'], unique=False)
    op.create_index(op.f('ix_blogcomment_user_id'), 'blogcomment', ['user_id'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_blogcomment_user_id'), table_name='blogcomment')
    op.drop_index(op.f('ix_blogcomment_id'), table_name='blogcomment')
    op.drop_index(op.f('ix_blogcomment_blog_id'), table_name='blogcomment')
    op.drop_table('blogcomment')
    op.drop_index(op.f('ix_blog_posted_by_id'), table_name='blog')
    op.drop_index(op.f('ix_blog_id'), table_name='blog')
    op.drop_table('blog')
    op.drop_index(op.f('ix_user_id'), table_name='user')
    op.drop_index(op.f('ix_user_email'), table_name='user')
    op.drop_table('user')
    # ### end Alembic commands ###
