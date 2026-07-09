from PySide6.QtCore import Qt
from PySide6.QtWidgets import QPushButton


class PrimaryButton(QPushButton):
    """
    Botón principal de la aplicación.
    """

    def __init__(self, text: str):
        super().__init__(text)

        self.setMinimumHeight(48)
        self.setCursor(Qt.PointingHandCursor)

        self.setStyleSheet("""
            QPushButton {

                background-color: #2DA8FF;
                color: white;
                border: none;
                border-radius: 8px;
                font-size: 14px;
                font-weight: bold;
                padding: 10px 20px;
            }

            QPushButton:hover {

                background-color: #47B7FF;
            }

            QPushButton:pressed {

                background-color: #168FE5;
            }

        """)