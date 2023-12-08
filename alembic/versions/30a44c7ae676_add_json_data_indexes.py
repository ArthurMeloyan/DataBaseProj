"""add json data indexes

Revision ID: 30a44c7ae676
Revises: 84b51d63acb8
Create Date: 2023-12-09 01:48:53.611320

"""
from typing import Sequence, Union
from sqlalchemy.dialects.postgresql import JSONB
from sqlalchemy.sql import text
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '30a44c7ae676'
down_revision: Union[str, None] = '84b51d63acb8'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade():
    op.execute("CREATE EXTENSION IF NOT EXISTS pg_trgm;")
    op.execute("CREATE INDEX idx_json_data_json_field_gin_trgm ON json_data USING gin (json_field jsonb_path_ops);")


def downgrade():
    pass
