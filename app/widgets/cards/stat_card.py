from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout,
    QScrollArea
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

        self.icon = QLabel(icon)
        self.icon.setObjectName("StatCardIcon")
        self.icon.setAlignment(Qt.AlignCenter)
        self.icon.setFont(QFont("Segoe UI Emoji", 20))

        self.title = QLabel(title)
        self.title.setObjectName("StatCardTitle")
        self.title.setAlignment(Qt.AlignCenter)

        text = value if not unit else f"{value} {unit}"
        self.value = QLabel(text)
        self.value.setObjectName("StatCardValue")
        self.value.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.icon)
        layout.addWidget(self.title)
        layout.addWidget(self.value)
        

        if status:
            self.setProperty("status", status)
            self.style().unpolish(self)
            self.style().polish(self)