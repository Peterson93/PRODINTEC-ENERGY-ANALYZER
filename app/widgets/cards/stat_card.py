from PySide6.QtCore import Qt
from PySide6.QtGui import QFont, QIcon
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class StatCard(QFrame):

    def __init__(self, title, value, unit="", icon="", status=None):
        super().__init__()

        self.setObjectName("StatCard")
        self.setMinimumWidth(130)
        self.setMaximumHeight(100)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(6)
        layout.setContentsMargins(10, 10, 10, 10)

        # -----------------------------
        # Icono
        # -----------------------------

        self.icon = QLabel()
        self.icon.setObjectName("StatCardIcon")
        self.icon.setAlignment(Qt.AlignCenter)

        if icon:
            self.icon.setPixmap(
                QIcon(icon).pixmap(24, 24)
            )

        # -----------------------------
        # Título
        # -----------------------------

        self.title = QLabel(title)
        self.title.setObjectName("StatCardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        # -----------------------------
        # Valor + unidad
        # -----------------------------

        text = value if not unit else f"{value} {unit}"

        self.value = QLabel(text)
        self.value.setObjectName("StatCardValue")
        self.value.setAlignment(Qt.AlignCenter)

        # -----------------------------
        # Layout
        # -----------------------------

        layout.addWidget(self.icon)
        layout.addWidget(self.title)
        layout.addWidget(self.value)

        # -----------------------------
        # Estado
        # -----------------------------

        if status:
            self.setProperty("status", status)

            self.style().unpolish(self)
            self.style().polish(self)