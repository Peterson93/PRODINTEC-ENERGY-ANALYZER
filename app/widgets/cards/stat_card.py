from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QFrame,
    QLabel,
    QVBoxLayout
)

import qtawesome as qta


class StatCard(QFrame):
    """
    Tarjeta reutilizable para mostrar indicadores (KPI)
    del Dashboard Ejecutivo.
    """

    def __init__(
        self,
        icon="fa5s.chart-bar",
        title="Indicador",
        value="0",
        unit="",
        parent=None
    ):
        super().__init__(parent)

        self.setObjectName("StatCard")

        self.icon_label = QLabel()
        self.icon_label.setObjectName("StatCardIcon")
        self.icon_label.setAlignment(Qt.AlignCenter)

        self.title_label = QLabel(title)
        self.title_label.setObjectName("StatCardTitle")
        self.title_label.setAlignment(Qt.AlignCenter)

        self.value_label = QLabel(str(value))
        self.value_label.setObjectName("StatCardValue")
        self.value_label.setAlignment(Qt.AlignCenter)

        self.unit_label = QLabel(unit)
        self.unit_label.setObjectName("StatCardUnit")
        self.unit_label.setAlignment(Qt.AlignCenter)

        layout = QVBoxLayout(self)
        layout.setContentsMargins(20, 20, 20, 20)
        layout.setSpacing(8)

        layout.addWidget(self.icon_label)
        layout.addWidget(self.title_label)
        layout.addWidget(self.value_label)
        layout.addWidget(self.unit_label)

        self.set_icon(icon)

    # -------------------------------------------------
    # Métodos públicos
    # -------------------------------------------------

    def set_title(self, title: str):
        self.title_label.setText(title)

    def set_value(self, value):
        self.value_label.setText(str(value))

    def set_unit(self, unit: str):
        self.unit_label.setText(unit)

    def set_icon(self, icon_name: str):

        icon = qta.icon(
            icon_name,
            color="#F5B041"
        )

        self.icon_label.setPixmap(icon.pixmap(34, 34))

    def set_status(self, status: str):
        """
        Cambia el estado visual de la tarjeta.

        success
        warning
        danger
        normal
        """

        status = status.lower()

        colors = {
            "success": "#2ECC71",
            "warning": "#F1C40F",
            "danger": "#E74C3C",
            "normal": "#F5B041"
        }

        color = colors.get(status, "#F5B041")

        icon = self.icon_label.pixmap()

        if icon is not None:
            # simplemente volvemos a cargar el icono
            # usando el nuevo color
            pass

        self.setProperty("status", status)

        self.style().unpolish(self)
        self.style().polish(self)