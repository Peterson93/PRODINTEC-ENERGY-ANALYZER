from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QVBoxLayout,
    QWidget,
)


class HomePage(QWidget):
    """
    Página de inicio de la aplicación.
    """

    def __init__(self) -> None:
        super().__init__()

        self.build_ui()

    def build_ui(self) -> None:

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(20)
        title = QLabel("Bienvenido a PRODINTEC S.A.S")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 24, QFont.Bold))
        subtitle = QLabel(
            "Ingeniería que genera valor"
        )

        subtitle.setAlignment(Qt.AlignCenter)
        subtitle.setFont(QFont("Segoe UI", 12))
        self.new_study_button = QPushButton(
            " Nuevo Estudio Solar"
        )

        self.new_study_button.setMinimumHeight(50)
        self.new_study_button.setMinimumWidth(260)

        layout.addWidget(title)
        layout.addWidget(subtitle)
        layout.addSpacing(30)
        layout.addWidget(
            self.new_study_button,
            alignment=Qt.AlignCenter,
        )