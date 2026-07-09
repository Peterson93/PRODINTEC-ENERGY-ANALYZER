from app.engine.solar_engine import SolarEngine
from app.mappers.project_mapper import ProjectMapper


class StudyController:

    def __init__(self):
        self.engine = SolarEngine()

    def calculate(self, form):

        project = ProjectMapper.from_form(form)

        return self.engine.calculate(project)