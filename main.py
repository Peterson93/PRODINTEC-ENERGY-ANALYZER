import sys
from PySide6.QtWidgets import QApplication
from app.ui.main_window import MainWindow
from app.theme.stylesheet import load_stylesheet


def main():
    app = QApplication(sys.argv)

    # Aplicar el tema global
    app.setStyleSheet(load_stylesheet())

    window = MainWindow()
    window.show()

    sys.exit(app.exec())


if __name__ == "__main__":
    main()