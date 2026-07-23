from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QWidget,
)

from app.widgets.buttons.primary_button import PrimaryButton
from app.wizard.study_wizard import StudyWizard


class HomePage(QWidget):

    def __init__(self):
        super().__init__()

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        title = QLabel("Bienvenido a PRODINTEC")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        subtitle = QLabel(
            "Ingeniería que genera valor"
        )

        subtitle.setAlignment(Qt.AlignCenter)
        self.new_study_button = PrimaryButton(
            "Nuevo Estudio Solar"
        )

        self.new_study_button.clicked.connect(
            self.open_study_wizard
        )

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(
            self.new_study_button,
            alignment=Qt.AlignCenter,
        )

    def open_study_wizard(self):

        wizard = StudyWizard(self)
        wizard.exec()
