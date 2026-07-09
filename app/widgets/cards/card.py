from PySide6.QtWidgets import QFrame, QVBoxLayout


class Card(QFrame):
    """
    Tarjeta base reutilizable para la aplicación.
    """

    def __init__(self):
        super().__init__()

        self.setObjectName("Card")
        self.layout = QVBoxLayout(self)
        self.layout.setContentsMargins(20, 20, 20, 20)
        self.layout.setSpacing(15)
        self.setStyleSheet("""
            QFrame#Card{

                background:#252525;
                border:1px solid #363636;
                border-radius:12px;

            }
        """)