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
    def calculate_tir(cash_flows, guess=0.10):
    
                rate = guess
    
                for _ in range(100):
    
                    npv = 0
                    derivative = 0
    
                    for year, cash_flow in enumerate(cash_flows):
    
                        npv += cash_flow / ((1 + rate) ** year)
    
                        if year > 0:
                            derivative -= (
                                year
                                * cash_flow
                                / ((1 + rate) ** (year + 1))
                            )
    
                    if abs(derivative) < 1e-10:
                        break
    
                    new_rate = rate - npv / derivative
    
                    if abs(new_rate - rate) < 1e-7:
                        rate = new_rate
                        break
    
                    rate = new_rate
    
                return rate

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
                * project.solar_system.performance_ratio
                * 30
            )
        )

        # 3. Número de paneles
        
        panel_count = ceil(
            required_power * 1000
            / project.solar_system.panel_power_wp
        )

        # 4. Potencia realmente instalada

        installed_power = (
            panel_count
            * project.solar_system.panel_power_wp
            / 1000
        )

        # 5. Área requerida

        required_area = (
            panel_count
            * project.solar_system.panel_area_m2
        )
        
        # 6. Generación mensual estimada

        monthly_generation = (
            installed_power
            * project.peak_sun_hours
            * project.solar_system.performance_ratio
            * 30
        )
        
        # 7. Generación anual estimada
        
        annual_generation = monthly_generation * 12

        # Distribución mensual estimada (%)
        monthly_profile = [
            0.085,
            0.082,
            0.086,
            0.081,
            0.080,
            0.083,
            0.086,
            0.087,
            0.082,
            0.080,
            0.079,
            0.089,
        ]

        monthly_generation_list = [
         round(annual_generation * factor, 1)
         for factor in monthly_profile
        ]

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

        # 11. Evaluación financiera

        discount_rate = project.discount_rate / 100
        energy_price_increase = project.annual_energy_price_increase / 100
        panel_degradation = project.annual_panel_degradation / 100
        maintenance_percent = project.annual_maintenance_percent / 100

        life_years = project.project_lifetime_years

        van = -estimated_investment

        cash_flows = [-estimated_investment]

        for year in range(1, life_years + 1):

            # Generación anual considerando degradación
            generation_year = (
            annual_generation
            * ((1 - panel_degradation) ** (year - 1))
            )

            # Tarifa eléctrica considerando incremento anual
            tariff_year = (
            project.average_tariff
            * ((1 + energy_price_increase) ** (year - 1))
            )

            # Ahorro bruto del año
            savings_year = generation_year * tariff_year

            # Mantenimiento anual
            maintenance_year = (
            estimated_investment
            * maintenance_percent
            )

            # Flujo de caja neto
            cash_flow = savings_year - maintenance_year

            cash_flows.append(cash_flow)

            print(
            "AÑO:",
            year,
            "GENERACIÓN:",
            generation_year,
            "TARIFA:",
            tariff_year,
            "AHORRO:",
            savings_year,
            "MANTENIMIENTO:",
            maintenance_year,
            "FLUJO:",
            cash_flow
            )

            # Valor presente del flujo
            present_value = (
            cash_flow
            / ((1 + discount_rate) ** year)
            )

            van += present_value

        tir = SolarEngine.calculate_tir(cash_flows)
        tir_percent = tir * 100

        

        print("=" * 40)
        print("Potencia instalada:", installed_power)
        print("Inversión:", estimated_investment)
        print("Generación mensual:", monthly_generation)
        print("Tarifa:", project.average_tariff)
        print("Ahorro mensual:", monthly_savings)
        print("Ahorro anual:", annual_savings)
        print("=" * 40)

       # 11. Payback

        if annual_savings > 0:
            payback = estimated_investment / annual_savings
        else:
            payback = 0

        # 12. ROI

        if estimated_investment > 0:
            roi = (annual_savings / estimated_investment) * 100
        else:
            roi = 0

        

        # viabilidad

        if payback <= 5:

            viability = "🟢 Alta"

        elif payback <= 7:

            viability = "🟡 Media"

        else:

            viability = "🔴 Baja"

        # 13. CO₂ evitado

        co2_avoided = annual_generation * 0.00018

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
        result.tir = round(tir_percent,1)

        print("=" * 50)
        print("EVALUACIÓN FINANCIERA")
        print("Inversión:", estimated_investment)
        print("Ahorro anual inicial:", annual_savings)
        print("Tasa descuento:", project.discount_rate)
        print("Incremento tarifa:", project.annual_energy_price_increase)
        print("Degradación:", project.annual_panel_degradation)
        print("Mantenimiento:", project.annual_maintenance_percent)
        print("Vida útil:", project.project_lifetime_years)
        print("VAN:", van)
        print("=" * 50)

        result.van = round(van)
        result.co2_avoided_tons = round(co2_avoided, 2)
        result.viability = viability

        result.cash_flows = [
        round(value)
        for value in cash_flows
        ]

        result.monthly_generation = monthly_generation_list
  
        return result