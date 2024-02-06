"""Init

Revision ID: c2e384e96b18
Revises: 
Create Date: 2024-02-06 17:35:27.883334

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'c2e384e96b18'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('contacts',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('firstname', sa.String(length=50), nullable=False),
    sa.Column('lastname', sa.String(length=50), nullable=False),
    sa.Column('email', sa.String(length=50), nullable=False),
    sa.Column('phone', sa.String(length=25), nullable=False),
    sa.Column('birthday', sa.Date(), nullable=False),
    sa.Column('completed', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_contacts_birthday'), 'contacts', ['birthday'], unique=False)
    op.create_index(op.f('ix_contacts_email'), 'contacts', ['email'], unique=False)
    op.create_index(op.f('ix_contacts_firstname'), 'contacts', ['firstname'], unique=False)
    op.create_index(op.f('ix_contacts_lastname'), 'contacts', ['lastname'], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_contacts_lastname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_firstname'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_email'), table_name='contacts')
    op.drop_index(op.f('ix_contacts_birthday'), table_name='contacts')
    op.drop_table('contacts')
    # ### end Alembic commands ###
