from dataclasses import dataclass


@dataclass
class StudyForm:

    # Cliente
    company: str = ""
    contact: str = ""

    # Energía
    monthly_consumption_kwh: float = 0.0
    average_tariff: float = 0.0
    target_coverage: float = 90.0

    # Sitio
    department: str = ""
    city: str = ""
    available_area_m2: float = 0.0

    # Sistema
    panel_power_wp: float = 550