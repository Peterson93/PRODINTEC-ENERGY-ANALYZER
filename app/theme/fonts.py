from PySide6.QtGui import QFont


class Fonts:

    @staticmethod
    def h1():

        return QFont("Segoe UI", 22, QFont.Bold)

    @staticmethod
    def h2():

        return QFont("Segoe UI", 16, QFont.Bold)

    @staticmethod
    def body():

        return QFont("Segoe UI", 10)

    @staticmethod
    def button():

        return QFont("Segoe UI", 10, QFont.Bold)