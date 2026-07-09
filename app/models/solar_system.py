from dataclasses import dataclass


@dataclass
class SolarSystem:

    panel_brand: str = "LONGi"
    panel_model: str = "LR5-72HPH-550M"
    panel_power_wp: float = 550
    panel_area_m2: float = 2.58
    performance_ratio: float = 0.80