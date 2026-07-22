from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
)


class StatCard(QFrame):

    def __init__(self, title, value, unit="", icon="", status=None):
        super().__init__()

        self.setObjectName("StatCard")
        self.setMinimumSize(240, 170)

        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setSpacing(10)
        layout.setContentsMargins(15, 15, 15, 15)

        self.icon = QLabel(icon)
        self.icon.setObjectName("StatCardIcon")
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setFont(QFont("Segoe UI Emoji", 24))

        self.title = QLabel(title)
        self.title.setObjectName("StatCardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        self.value = QLabel(value)
        self.value.setObjectName("StatCardValue")
        self.value.setAlignment(Qt.AlignCenter)

        self.unit = QLabel(unit)
        self.unit.setObjectName("StatCardUnit")
        self.unit.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.icon)
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        layout.addWidget(self.unit)

        if status:
            self.setProperty("status", status)
            self.style().unpolish(self)
            self.style().polish(self)