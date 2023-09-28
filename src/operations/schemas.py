from pydantic import BaseModel


class ConstParamsCreate(BaseModel):
    id: int
    time_max: int
    time_variable: int
    tablet_diameter: float
    tablet_height: float
    bunker_volume: int
    delta_force_press: float
    delta_powder_density: float
    max_pallet: int
    ppr_time_max: int
    experiment_tag: str
    
    
class VariableParamsCreate(BaseModel):
    id : int
    speed_in_press: float
    speed_out_press: float
    force_press: float
    force_retention: float
    time_to_wait: float
    time_to_unloading: float
    press_number: int
    ppr_update: int
    time_delay_powder: float
    time_delay_pallet: float
    time_delay_ppr: float
    number_of_containers: int
    powder_density: float
    powder_mass: int
    signal_manual_control: int
    experiment_tag: str

    