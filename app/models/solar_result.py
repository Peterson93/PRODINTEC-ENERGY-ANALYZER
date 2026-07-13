from dataclasses import dataclass


@dataclass
class SolarResult:

    installed_power_kwp: float = 0.0
    panel_count: int = 0
    required_area_m2: float = 0.0
    monthly_generation_kwh: float = 0.0
    annual_generation_kwh: float = 0.0
    monthly_savings: float = 0.0
    annual_savings: float = 0.0
    estimated_investment: float = 0.0
    payback_years: float = 0.0
    roi: float = 0.0
    co2_avoided_tons: float = 0.0
    viability: str = ""