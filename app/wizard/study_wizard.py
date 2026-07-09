from PySide6.QtWidgets import (
    QDialog,
    QVBoxLayout,
    QStackedWidget,
    QHBoxLayout,
)

from app.widgets.buttons.primary_button import PrimaryButton


class StudyWizard(QDialog):

    def __init__(self, parent=None):
        super().__init__(parent)

        self.setWindowTitle("Nuevo Estudio Solar")
        self.resize(900, 650)
        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)
        self.stack = QStackedWidget()
        layout.addWidget(self.stack)
        navigation = QHBoxLayout()
        navigation.addStretch()
        self.previous_button = PrimaryButton("← Anterior")
        self.next_button = PrimaryButton("Siguiente →")
        navigation.addWidget(self.previous_button)
        navigation.addWidget(self.next_button)
        layout.addLayout(navigation)