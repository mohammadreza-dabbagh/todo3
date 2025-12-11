
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa

revision: str = 'be8ada8bd55a'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    
    op.create_table('projects',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name'),
    schema='public' 
    )
    op.create_index(op.f('ix_public_projects_id'), 'projects', ['id'], unique=False, schema='public')
    op.create_index(op.f('ix_public_projects_name'), 'projects', ['name'], unique=True, schema='public')

    
    op.create_table('tasks',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(), nullable=False),
    sa.Column('description', sa.String(), nullable=True),
    sa.Column('status', sa.String(), nullable=True),
    sa.Column('deadline', sa.DateTime(), nullable=False),
    sa.Column('closed_at', sa.DateTime(), nullable=True),
    sa.Column('project_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['project_id'], ['public.projects.id'], ), # مطمئن شوید اینجا هم public.projects باشد
    sa.PrimaryKeyConstraint('id'),
    schema='public' 
    )
    op.create_index(op.f('ix_public_tasks_id'), 'tasks', ['id'], unique=False, schema='public')

def downgrade() -> None:
    # مطمئن شوید اینها هم به schema='public' اشاره می‌کنند
    op.drop_index(op.f('ix_public_tasks_id'), table_name='tasks', schema='public')
    op.drop_table('tasks', schema='public')
    op.drop_index(op.f('ix_public_projects_name'), table_name='projects', schema='public')
    op.drop_index(op.f('ix_public_projects_id'), table_name='projects', schema='public')
    op.drop_table('projects', schema='public')