import os

print("STUDY CONTROLLER:", os.path.abspath(__file__))
from app.engine.solar_engine import SolarEngine
from app.mappers.project_mapper import ProjectMapper


class StudyController:

    def __init__(self):
        self.engine = SolarEngine()

    def calculate(self, form):

        project = ProjectMapper.from_form(form)

        result = self.engine.calculate(project)

        return result