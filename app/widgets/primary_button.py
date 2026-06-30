from PySide6.QtWidgets import QPushButton

from app.theme.fonts import Fonts


class PrimaryButton(QPushButton):

    def __init__(self, text):

        super().__init__(text)

        self.setMinimumHeight(46)

        self.setFont(Fonts.button())