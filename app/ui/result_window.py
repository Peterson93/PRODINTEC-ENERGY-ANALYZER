from PySide6.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QGridLayout,
    QHBoxLayout,
    QFrame,
    QScrollArea
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QFont
from app.widgets.cards.stat_card import StatCard
from app.widgets.charts.monthly_generation_chart import MonthlyGenerationChart
from app.widgets.cards.Metric_Card import MetricCard
from app.widgets.charts.cash_flow_chart import CashFlowChart

class ResultWindow(QWidget):

    def __init__(self, result):
        super().__init__()

        self.result = result

        self.setWindowTitle("Resultado del Estudio Solar")
        self.resize(1200, 700)

        self.build_ui()

    def build_ui(self):

        # Layout principal de la ventana
        main_layout = QVBoxLayout(self)

        # Área desplazable
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)

        main_layout.addWidget(scroll)

        # Contenedor del contenido
        content = QWidget()
        scroll.setWidget(content)

        # Layout donde irá todo el dashboard
        layout = QVBoxLayout(content)
        layout.setContentsMargins(30, 30, 30, 30)
        layout.setSpacing(15)

        title = QLabel("ESTUDIO PRELIMINAR")
        title.setAlignment(Qt.AlignCenter)
        title.setFont(QFont("Segoe UI", 20, QFont.Bold))

        layout.addWidget(title)

        if self.result.viability == "🟢 Alta":
            status = "success"
        elif self.result.viability == "🟡 Media":
            status = "warning"
        else:
            status = "danger"

        cards = [

        ("app/assets/icons/power.svg", "Potencia instalada",
        f"{self.result.installed_power_kwp}",
        "kWp", None),

        ("app/assets/icons/panels.svg", "Paneles",
        str(self.result.panel_count),
        "paneles", None),

        ("app/assets/icons/area.svg", "Área requerida",
        f"{self.result.required_area_m2}",
        "m²", None),

        ("app/assets/icons/generation.svg", "Generación mensual",
        f"{self.result.monthly_generation_kwh}",
        "kWh", None),

        ("app/assets/icons/generation_annual.svg", "Generación anual",
        f"{self.result.annual_generation_kwh}",
        "kWh", None),

        ("app/assets/icons/investment.svg", "Inversión",
        f"${self.result.estimated_investment:,.0f}",
        "COP", None),

        ("app/assets/icons/saving_monthly.svg", "Ahorro mensual",
        f"${self.result.monthly_savings:,.0f}",
        "COP", None),

        ("app/assets/icons/savings_annual.svg", "Ahorro anual",
        f"${self.result.annual_savings:,.0f}",
        "COP", None),

        ("app/assets/icons/payback.svg", "Payback",
        f"{self.result.payback_years}",
        "años", None),

        ("app/assets/icons/viability.svg",
        "Viabilidad",
        self.result.viability,
        "",
        status
        ),

        ("app/assets/icons/co2.svg",
        "CO₂ evitado",
        f"{self.result.co2_avoided_tons}",
        "ton/año",
        None
        ),
        ]

        grid = QGridLayout()

        grid.setContentsMargins(30, 20, 30, 20)
        grid.setHorizontalSpacing(6)
        grid.setVerticalSpacing(6)

        for index, card in enumerate(cards):

            icon, title, value, unit, status = card

            widget = StatCard(
                title=title,
                value=value,
                unit=unit,
                icon=icon,
                status=status
            )

            row = index // 3
            col = index % 3

            grid.addWidget(widget, row, col)

        layout.addLayout(grid)


        # ==========================================
        # PANEL DE ANÁLISIS
        # ==========================================

        graph_title = QLabel("GENERACIÓN MENSUAL")
        graph_title.setAlignment(Qt.AlignCenter)
        graph_title.setFont(QFont("Segoe UI", 15, QFont.Bold))

        layout.addSpacing(20)
        layout.addWidget(graph_title)

        graph_frame = QFrame()
        graph_frame.setObjectName("ResultCard")
        graph_frame.setMinimumHeight(320)

        graph_layout = QVBoxLayout(graph_frame)

        chart = MonthlyGenerationChart(self.result)
        chart.setMinimumHeight(280)

        graph_layout.addWidget(chart)

        layout.addWidget(graph_frame)

        # ==========================================
        # FLUJO DE CAJA
        # ==========================================

        cash_title = QLabel("FLUJO DE CAJA ACUMULADO")
        cash_title.setAlignment(Qt.AlignCenter)
        cash_title.setFont(QFont("Segoe UI", 15, QFont.Bold))

        layout.addSpacing(20)
        layout.addWidget(cash_title)

        cash_frame = QFrame()
        cash_frame.setObjectName("ResultCard")
        cash_frame.setMinimumHeight(400)

        cash_layout = QVBoxLayout(cash_frame)
        cash_layout.setContentsMargins(15, 15, 15, 15)

        cash_chart = CashFlowChart(self.result)

        cash_layout.addWidget(cash_chart,1)

        layout.addWidget(cash_frame)

        # INDICADORES FINANCIEROS

        finance_title = QLabel("INDICADORES FINANCIEROS")
        finance_title.setAlignment(Qt.AlignCenter)
        finance_title.setFont(QFont("Segoe UI", 15, QFont.Bold))

        layout.addSpacing(20)
        layout.addWidget(finance_title)

        finance_layout = QHBoxLayout()
        finance_layout.setSpacing(20)

        roi_card = MetricCard(
            "ROI",
            f"{self.result.roi} %",
            "Retorno anual",
             "#4CAF50"
        )

        van_card = MetricCard(
            "VAN",
            f"${self.result.van:,.0f}",
            "valor actual neto",
             "#2196F3"
        )

        tir_card = MetricCard(
            "TIR",
            f"{self.result.tir:,.0f} %",
            "Tasa interna de retorno",
             "#4CAF50"
        )
        

        finance_layout.addWidget(roi_card)
        finance_layout.addWidget(van_card)
        finance_layout.addWidget(tir_card)
         
        layout.addLayout(finance_layout)

      

       

        

        