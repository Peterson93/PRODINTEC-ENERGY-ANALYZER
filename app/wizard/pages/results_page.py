from PySide6.QtWidgets import (
    QWidget,
    QGridLayout,
)

from app.widgets.cards.stat_card import StatCard

class ResultsPage(QWidget):

    def __init__(self):

        super().__init__()

        layout = QGridLayout(self)

        self.power = StatCard(
            "Potencia",
            "--"
        )

        self.panels = StatCard(
            "Paneles",
            "--"
        )

        self.area = StatCard(
            "Área",
            "--"
        )

        self.energy = StatCard(
            "Generación",
            "--"
        )

        layout.addWidget(self.power,0,0)
        layout.addWidget(self.panels,0,1)
        layout.addWidget(self.area,1,0)
        layout.addWidget(self.energy,1,1)

def load_result(self, result):

    self.power.set_value(
        f"{result.installed_power_kwp} kWp"
    )

    self.panels.set_value(
        result.panel_count
    )

    self.area.set_value(
        f"{result.required_area_m2} m²"
    )

    self.energy.set_value(
        f"{result.monthly_generation_kwh:.0f} kWh/mes"
    )