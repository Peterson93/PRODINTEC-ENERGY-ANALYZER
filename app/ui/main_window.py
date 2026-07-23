from PySide6.QtWidgets import (
    QHBoxLayout,
    QVBoxLayout,
    QMainWindow,
    QWidget,
    QStackedWidget,
)

from app.ui.home_page import HomePage
from app.widgets.navigation_panel import NavigationPanel
from app.widgets.topbar import TopBar


class MainWindow(QMainWindow):
    """
    Ventana principal de la aplicación.
    Su única responsabilidad es organizar los componentes principales.
    """

    def __init__(self) -> None:
        super().__init__()

        self.setWindowTitle("PRODINTEC Energy Analyzer")
        self.resize(1400, 850)
        self.setMinimumSize(1200, 700)
        self.build_ui()

    def build_ui(self) -> None:

        # ---------- Widget Central ----------

        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        root_layout = QHBoxLayout(central_widget)
        root_layout.setContentsMargins(0, 0, 0, 0)
        root_layout.setSpacing(0)

        # ---------- Menú lateral ----------

        self.navigation_panel = NavigationPanel()
        root_layout.addWidget(self.navigation_panel)

        # ---------- Área derecha ----------

        right_container = QWidget()
        right_layout = QHBoxLayout(right_container)
        right_layout.setContentsMargins(0, 0, 0, 0)
        right_layout.setSpacing(0)
        root_layout.addWidget(right_container)

        # ---------- Contenedor principal ----------

        main_container = QWidget()
        main_layout = QVBoxLayout(main_container)
        main_layout.setContentsMargins(0, 0, 0, 0)
        main_layout.setSpacing(0)

        # ---------- Barra superior ----------

        self.top_bar = TopBar()
        main_layout.addWidget(self.top_bar)

        # ---------- Páginas ----------

        self.stack = QStackedWidget()
        self.home_page = HomePage()
        self.stack.addWidget(self.home_page)
        main_layout.addWidget(self.stack)
        right_layout.addWidget(main_container)