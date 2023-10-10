from sqlalchemy import Table, Column, Integer, Float, MetaData, String

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
    Column("SpeedInPress", Float),
    Column("SpeedOutPress", Float),
    Column("ForcePress", Float),
    Column("ForceRetention", Float),
    Column("TimeToWait", Float),
    Column("TimeToUnloading", Float),
    Column("PressNumber", Integer),
    Column("PprUpdate", Integer),
    Column("TimeDelayPowder", Float),
    Column("TimeDelayPallet", Float),
    Column("TimeDelayPpr", Float),
    Column("NumberOfContainers", Integer),
    Column("PowderDensity", Float),
    Column("PowderMass", Integer),
    Column("SignalManualControl", Integer),
    Column("experiment_tag", String)
)