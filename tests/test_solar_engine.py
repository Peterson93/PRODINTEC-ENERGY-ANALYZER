from app.engine.solar_engine import SolarEngine
from app.models.project import Project

project = Project(
    monthly_consumption_kwh=2500,
    target_coverage=90,
    peak_sun_hours=5.2,
    average_tariff=980,
    )

result = SolarEngine.calculate(project)

print("=" * 40)
print("RESULTADOS DEL CÁLCULO")
print("=" * 40)

print(f"Potencia instalada : {result.installed_power_kwp} kWp")
print(f"Paneles            : {result.panel_count}")
print(f"Área requerida     : {result.required_area_m2} m²")
print(f"Generación mensual : {result.monthly_generation_kwh} kWh")
print(f"Generación anual   : {result.annual_generation_kwh} kWh")
print(f"Inversión          : ${result.estimated_investment:,.0f}")
print(f"Ahorro mensual     : ${result.monthly_savings:,.0f}")
print(f"Ahorro anual       : ${result.annual_savings:,.0f}")
print(f"Payback            : {result.payback_years} años")
print(f"ROI                : {result.roi}%")
print(f"Viabilidad         : {result.viability}")