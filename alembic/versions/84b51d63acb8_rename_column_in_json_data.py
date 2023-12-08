"""rename column in json data

Revision ID: 84b51d63acb8
Revises: 16df33f50b19
Create Date: 2023-12-09 01:27:35.034658

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '84b51d63acb8'
down_revision: Union[str, None] = '16df33f50b19'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    op.alter_column('json_data', 'name', new_column_name='json_field')


def downgrade() -> None:
    pass
