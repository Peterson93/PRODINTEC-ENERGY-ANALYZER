from dataclasses import dataclass,field
from datetime import datetime
from app.models.location import Location
from app.models.solar_system import SolarSystem

@dataclass
class Project:

    # datos del proyecto
    project_id: str = ""
    project_name: str = ""
    created_at: datetime = field(
    default_factory=datetime.now
    )

    # Datos del cliente
    company: str = ""
    contact: str = ""

    # Consumo
    monthly_consumption_kwh: float = 0.0
    average_tariff: float = 0.0
    target_coverage: float = 90.0

    # Recurso solar
    peak_sun_hours: float = 5.2
    location: Location = field(default_factory=Location)

    # Panel seleccionado
    solar_system: SolarSystem = field(default_factory=SolarSystem)

   
    # Costos

    cost_per_kwp = 3_800_000
    annual_energy_price_increase = 6.0
    annual_maintenance_percent = 1.0
    annual_panel_degradation = 0.5

    # Resultados
    installed_power_kwp: float = 0.0
    panel_count: int = 0
    required_area_m2: float = 0.0
    monthly_generation_kwh: float = 0.0
    annual_generation_kwh: float = 0.0