from sqlalchemy import Table, Column, Integer, Float, String

from src.database import metadata

input_const_params = Table(
    "input_const",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("time_max", Integer),
    Column("time_variable", Integer),
    Column("tablet_diameter", Float),
    Column("tablet_height", Float),
    Column("bunker_volume", Integer),
    Column("delta_force_press", Float),
    Column("delta_powder_density", Float),
    Column("max_pallet", Integer),
    Column("ppr_time_max", Integer),
    Column("experiment_tag", String)
)

input_variable_params = Table(
    "input_variable",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("speed_in_press", Float),
    Column("speed_out_press", Float),
    Column("force_press", Float),
    Column("force_retention", Float),
    Column("time_to_wait", Float),
    Column("time_to_unloading", Float),
    Column("press_number", Integer),
    Column("ppr_update", Integer),
    Column("time_delay_powder", Float),
    Column("time_delay_pallet", Float),
    Column("time_delay_ppr", Float),
    Column("number_of_containers", Integer),
    Column("powder_density", Float),
    Column("powder_mass", Integer),
    Column("signal_manual_control", Integer),
    Column("experiment_tag", String)
)