from dataclasses import dataclass


@dataclass
class Panel:

    manufacturer: str

    model: str

    power_wp: float

    efficiency: float

    area_m2: float