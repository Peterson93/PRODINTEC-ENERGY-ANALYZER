from app.theme.colors import Colors


def load_stylesheet():

    return f"""

    QWidget {{
        background-color: {Colors.BACKGROUND};
        color: {Colors.LIGHT};
        font-family: Segoe UI;
        font-size: 10pt;
    }}

    QPushButton {{
        background-color: {Colors.PRIMARY};
        border-radius: 10px;
        padding: 10px;
        color: white;
        font-weight: bold;
    }}

    QPushButton:hover {{
        background-color: #42A5F5;
    }}

    QPushButton:pressed {{
        background-color: #1565C0;
    }}

    """