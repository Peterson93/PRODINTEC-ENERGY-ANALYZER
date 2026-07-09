from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from PySide6.QtWidgets import (
    QLabel,
    QVBoxLayout,
    QFrame,
)


class StatCard(QFrame):

    def __init__(self, title, value):

        super().__init__()

        self.setObjectName("StatCard")
        self.setMinimumSize(220, 140)
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        self.title = QLabel(title)
        self.title.setAlignment(Qt.AlignCenter)
        self.title.setFont(QFont("Segoe UI", 11))
        self.value = QLabel(value)
        self.value.setAlignment(Qt.AlignCenter)
        self.value.setFont(QFont("Segoe UI", 22, QFont.Bold))
        layout.addWidget(self.title)
        layout.addSpacing(10)
        layout.addWidget(self.value)
        self.setStyleSheet("""
        QFrame#StatCard{

            background:#252525;

            border-radius:12px;

            border:1px solid #3A3A3A;

        }

        QLabel{

            color:white;

        }
        """)

    def set_value(self, value):

        self.value.setText(str(value))