from app.models.project import Project
from app.models.forms.study_form import StudyForm


class ProjectMapper:

    @staticmethod
    def from_form(form: StudyForm) -> Project:

        project = Project()

        project.company = form.company
        project.contact = form.contact

        project.monthly_consumption_kwh = form.monthly_consumption_kwh
        project.average_tariff = form.average_tariff
        project.target_coverage = form.target_coverage

        project.location.department = form.department
        project.location.city = form.city

        project.location.available_area_m2 = form.available_area_m2

        project.solar_system.panel_power_wp = form.panel_power_wp

        print("=" * 50)
        print("PROJECT CREADO")
        print(project)
        print("=" * 50)

        return project