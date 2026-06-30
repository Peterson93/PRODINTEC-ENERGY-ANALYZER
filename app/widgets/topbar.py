from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QHBoxLayout,
    QLabel,
    QWidget,
)


class TopBar(QWidget):
    """
    Barra superior de la aplicación.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setFixedHeight(60)
        self.build_ui()

    def build_ui(self) -> None:

        layout = QHBoxLayout(self)
        layout.setContentsMargins(20, 10, 20, 10)
        layout.setSpacing(10)

        # -------- Título --------

        title = QLabel("PRODINTEC Energy Analyzer")
        title.setFont(QFont("Segoe UI", 14, QFont.Bold))
        layout.addWidget(title)

        # -------- Espacio --------

        layout.addStretch()

        # -------- Versión --------

        version = QLabel("v0.1.0")
        version.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        layout.addWidget(version)