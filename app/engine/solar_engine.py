"""
Motor de cálculo preliminar para sistemas de generación solar fotovoltaicos.

Sprint 4 - Versión 0.1
"""

from math import ceil
from app.models.project import Project
from app.models.solar_result import SolarResult


class SolarEngine:
    """
    Motor encargado de realizar el cálculo preliminar de un sistema
    de generación solar fotovoltaico.
    """

    @staticmethod
    def calculate(project: Project) -> SolarResult:
        """
        Calcula el dimensionamiento preliminar del sistema.

        Parámetros
        ----------
        project : Project
            Información ingresada por el usuario.

        Retorna
        -------
        SolarResult
            Resultados del dimensionamiento.
        """

        result = SolarResult()

        # 1. Energía objetivo

        target_energy = (
            project.monthly_consumption_kwh
            * project.target_coverage
            / 100
        )
        
        # 2. Potencia requerida (kWp)
        
        # Fórmula:

        # P = E / (HSP × PR × 30)
        
        required_power = (
            target_energy
            / (
                project.peak_sun_hours
                * project.performance_ratio
                * 30
            )
        )

        # 3. Número de paneles
        
        panel_count = ceil(
            required_power * 1000
            / project.panel_power_wp
        )

        # 4. Potencia realmente instalada

        installed_power = (
            panel_count
            * project.panel_power_wp
            / 1000
        )

        # 5. Área requerida

        required_area = (
            panel_count
            * project.panel_area_m2
        )
        
        # 6. Generación mensual estimada

        monthly_generation = (
            installed_power
            * project.peak_sun_hours
            * project.performance_ratio
            * 30
        )
        
        # 7. Generación anual estimada
        
        annual_generation = monthly_generation * 12

        # 8.inversion

        estimated_investment = (
        installed_power
         * project.cost_per_kwp
        )
        # 9. ahorro mensual

        monthly_savings = (
         monthly_generation
        * project.average_tariff
        )

        # 10. ahorro anual

        annual_savings = (
        monthly_savings
        * 12
        )

        # 11. payback

        payback = (
        estimated_investment
        / annual_savings
        )

        # 12.ROI

        roi = (
        annual_savings
        / estimated_investment
        ) * 100

        # viabilidad

        if payback <= 5:

            viability = "🟢 Alta"

        elif payback <= 7:

            viability = "🟡 Media"

        else:

            viability = "🔴 Baja"
        
        # . Guardar resultados
        
        result.installed_power_kwp = round(installed_power, 2)
        result.panel_count = panel_count
        result.required_area_m2 = round(required_area, 2)
        result.monthly_generation_kwh = round(monthly_generation, 1)
        result.annual_generation_kwh = round(annual_generation, 1)
        result.estimated_investment = round(estimated_investment)
        result.monthly_savings = round(monthly_savings)
        result.annual_savings = round(annual_savings)
        result.payback_years = round(payback,1,)
        result.roi = round(roi,1,)
        result.viability = viability

        # Estos cálculos se implementarán en el Sprint 5

        result.monthly_savings = 0.0
        result.annual_savings = 0.0
        result.estimated_investment = 0.0
        result.payback_years = 0.0
        result.roi = 0.0
        result.co2_avoided_tons = 0.0
        result.viability = ""

        return result