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

        ("⚡", "Potencia instalada",
        f"{self.result.installed_power_kwp}",
        "kWp", None),

        (" ", "Paneles",
        str(self.result.panel_count),
        "paneles", None),

        ("📐", "Área requerida",
        f"{self.result.required_area_m2}",
        "m²", None),

        ("☀️", "Generación mensual",
        f"{self.result.monthly_generation_kwh}",
        "kWh", None),

        ("📈", "Generación anual",
        f"{self.result.annual_generation_kwh}",
        "kWh", None),

        ("💰", "Inversión",
        f"${self.result.estimated_investment:,.0f}",
        "COP", None),

        ("💵", "Ahorro mensual",
        f"${self.result.monthly_savings:,.0f}",
        "COP", None),

        ("💸", "Ahorro anual",
        f"${self.result.annual_savings:,.0f}",
        "COP", None),

        ("⏳", "Payback",
        f"{self.result.payback_years}",
        "años", None),

        ("📊", "ROI",
        f"{self.result.roi}",
        "%", None),

        (
        "📋",
        "Viabilidad",
        self.result.viability,
        "",
        status
        ),

        (
        "🌱",
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

        bottom_layout = QHBoxLayout()
        bottom_layout.setSpacing(10)

        left_panel = QFrame()
        left_panel.setObjectName("ResultCard")
        left_panel.setMinimumHeight(260)

        left_layout = QVBoxLayout(left_panel)

        left_title = QLabel("Generación mensual")
        left_title.setAlignment(Qt.AlignCenter)
        left_title.setFont(QFont("Segoe UI", 12, QFont.Bold))

        left_layout.addWidget(left_title)

        chart = MonthlyGenerationChart(self.result)
        left_layout.addWidget(chart)

        right_panel = QFrame()
        right_panel.setObjectName("ResultCard")
        right_panel.setMinimumHeight(260)

        bottom_layout.addWidget(left_panel, 3)
        bottom_layout.addWidget(right_panel, 1)

        right_layout = QVBoxLayout(right_panel)

        right_title = QLabel("Indicadores financieros")
        right_title.setAlignment(Qt.AlignCenter)
        right_title.setFont(QFont("Segoe UI", 12, QFont.Bold))

        right_layout.addWidget(right_title)
        right_layout.addStretch()

        layout.addLayout(bottom_layout)

        # ==========================================
        # PANEL DE ANÁLISIS
        # ==========================================

        analysis_title = QLabel("ANÁLISIS ENERGÉTICO")
        analysis_title.setAlignment(Qt.AlignCenter)
        analysis_title.setFont(QFont("Segoe UI", 16, QFont.Bold))

        layout.addSpacing(10)
        layout.addWidget(analysis_title)

        analysis_frame = QFrame()
        analysis_frame.setObjectName("ResultCard")

        analysis_layout = QVBoxLayout(analysis_frame)

        analysis_label = QLabel(
        "Aquí se visualizarán los gráficos del estudio."
        )

        analysis_label.setAlignment(Qt.AlignCenter)
        analysis_label.setFont(QFont("Segoe UI", 11))

        analysis_layout.addStretch()
        analysis_layout.addWidget(analysis_label)
        analysis_layout.addStretch()

        layout.addWidget(analysis_frame)

       

        

        