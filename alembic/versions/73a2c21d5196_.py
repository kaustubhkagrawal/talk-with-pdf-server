"""empty message

Revision ID: 73a2c21d5196
Revises: 268f5bded8c7
Create Date: 2024-01-18 19:27:06.617312

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision: str = '73a2c21d5196'
down_revision: Union[str, None] = '268f5bded8c7'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('document', sa.Column('name', sa.String(), nullable=True))
    op.add_column('document', sa.Column('assistant_id', sa.String(), nullable=True))
    op.create_unique_constraint(None, 'document', ['assistant_id'])
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(None, 'document', type_='unique')
    op.drop_column('document', 'assistant_id')
    op.drop_column('document', 'name')
    # ### end Alembic commands ###
