"""db init

Revision ID: 56ccbae6c841
Revises: 
Create Date: 2023-09-28 15:30:56.747950

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '56ccbae6c841'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('role',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=False),
    sa.Column('permissions', sa.JSON(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('registered_at', sa.TIMESTAMP(), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.Column('hashed_password', sa.String(), nullable=False),
    sa.Column('is_active', sa.Boolean(), nullable=False),
    sa.Column('is_superuser', sa.Boolean(), nullable=False),
    sa.Column('is_verified', sa.Boolean(), nullable=False),
    sa.ForeignKeyConstraint(['role_id'], ['role.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input_const',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('time_max', sa.Integer(), nullable=True),
    sa.Column('time_variable', sa.Integer(), nullable=True),
    sa.Column('tablet_diameter', sa.Float(), nullable=True),
    sa.Column('tablet_height', sa.Float(), nullable=True),
    sa.Column('bunker_volume', sa.Integer(), nullable=True),
    sa.Column('delta_force_press', sa.Float(), nullable=True),
    sa.Column('delta_powder_density', sa.Float(), nullable=True),
    sa.Column('max_pallet', sa.Integer(), nullable=True),
    sa.Column('ppr_time_max', sa.Integer(), nullable=True),
    sa.Column('experiment_tag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('input_variable',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('SpeedInPress', sa.Float(), nullable=True),
    sa.Column('SpeedOutPress', sa.Float(), nullable=True),
    sa.Column('ForcePress', sa.Float(), nullable=True),
    sa.Column('ForceRetention', sa.Float(), nullable=True),
    sa.Column('TimeToWait', sa.Float(), nullable=True),
    sa.Column('TimeToUnloading', sa.Float(), nullable=True),
    sa.Column('PressNumber', sa.Integer(), nullable=True),
    sa.Column('PprUpdate', sa.Integer(), nullable=True),
    sa.Column('TimeDelayPowder', sa.Float(), nullable=True),
    sa.Column('TimeDelayPallet', sa.Float(), nullable=True),
    sa.Column('TimeDelayPpr', sa.Float(), nullable=True),
    sa.Column('NumberOfContainers', sa.Integer(), nullable=True),
    sa.Column('PowderDensity', sa.Float(), nullable=True),
    sa.Column('PowderMass', sa.Integer(), nullable=True),
    sa.Column('SignalManualControl', sa.Integer(), nullable=True),
    sa.Column('experiment_tag', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('input_variable')
    op.drop_table('input_const')
    op.drop_table('user')
    op.drop_table('role')
    # ### end Alembic commands ###