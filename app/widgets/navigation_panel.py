from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QPushButton,
    QSizePolicy,
    QVBoxLayout,
    QWidget,
)


class NavigationPanel(QWidget):
    """
    Panel lateral de navegación.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setFixedWidth(200)
        self.build_ui()

    def build_ui(self) -> None:

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(12)

        # -------- Logo --------

        logo = QLabel("PRODINTEC S.A.S")
        logo.setAlignment(Qt.AlignCenter)
        logo.setFont(QFont("Segoe UI", 18, QFont.Bold))
        layout.addWidget(logo)
        layout.addSpacing(30)

        # -------- Botones --------

        self.home_button = QPushButton("Inicio")
        self.new_project_button = QPushButton("Nuevo Estudio")
        self.projects_button = QPushButton("Proyectos")
        self.settings_button = QPushButton("Configuración")

        buttons = [
            self.home_button,
            self.new_project_button,
            self.projects_button,
            self.settings_button,
        ]

        for button in buttons:

            button.setMinimumHeight(42)
            button.setCursor(Qt.PointingHandCursor)
            button.setSizePolicy(
                QSizePolicy.Expanding,
                QSizePolicy.Fixed,
            )

            layout.addWidget(button)

        layout.addStretch()