"""created_new_table_for_json_field

Revision ID: 16df33f50b19
Revises: 
Create Date: 2023-12-09 00:53:47.120134

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import JSONB
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '16df33f50b19'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.create_table(
        'json_data',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('name', JSONB),
    )


def downgrade() -> None:
    op.drop_table('json_data')
