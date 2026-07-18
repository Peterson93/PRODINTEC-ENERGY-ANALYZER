import os

print("STUDY WIZARD:", os.path.abspath(__file__))

from PySide6.QtWidgets import QWizard

from app.wizard.pages.client_page import ClientPage
from app.wizard.pages.consumption_page import ConsumptionPage
from app.models.forms.study_form import StudyForm
from app.controllers.study_controller import StudyController

class StudyWizard(QWizard):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.study_form = StudyForm()
        self.controller = StudyController()

        self.setWindowTitle("Nuevo Estudio")
        self.resize(900, 650)

        #  páginas
        self.client_page = ClientPage()
        self.consumption_page = ConsumptionPage()

        self.addPage(self.client_page)
        self.addPage(self.consumption_page)

        self.setOption(QWizard.NoBackButtonOnStartPage, True)

    def accept(self):

        self.study_form.monthly_consumption_kwh = (
        self.consumption_page.monthly_consumption.value()
    )

        self.study_form.average_tariff = (
        self.consumption_page.average_tariff.value()
    )

        self.study_form.target_coverage = (
        self.consumption_page.coverage.value()
    )

        result = self.controller.calculate(self.study_form)

        super().accept()