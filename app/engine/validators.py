class ProjectValidator:

    @staticmethod
    def validate(form):

        errors = []

        if form.monthly_consumption_kwh <= 0:
            errors.append("El consumo mensual debe ser mayor que cero.")

        if form.average_tariff <= 0:
            errors.append("La tarifa debe ser mayor que cero.")

        if not (1 <= form.target_coverage <= 100):
            errors.append("La cobertura debe estar entre 1 y 100 %.")

        if form.available_area_m2 <= 0:
            errors.append("Debe indicar el área disponible.")

        return errors