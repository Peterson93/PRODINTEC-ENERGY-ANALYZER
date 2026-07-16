from dataclasses import dataclass


@dataclass
class Location:

    country: str = "Colombia"
    department: str = ""
    city: str = ""
    latitude: float = 0.0
    longitude: float = 0.0
    peak_sun_hours: float = 5.2
    available_area_m2: float = 0.0