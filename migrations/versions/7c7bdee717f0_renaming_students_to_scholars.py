"""Renaming students to scholars

Revision ID: 7c7bdee717f0
Revises: 9419ab7aa1d5
Create Date: 2026-07-01 07:32:31.864069

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '7c7bdee717f0'
down_revision: Union[str, Sequence[str], None] = '9419ab7aa1d5'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    op.rename_table("students", "scholars")
    pass


def downgrade() -> None:
    """Downgrade schema."""
    op.rename_table("scholars", "students")
    pass
