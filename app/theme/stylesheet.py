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

    QFrame#StatCard{{

    background-color:#242424;
    border:1px solid #3A3A3A;
    border-radius:14px;
    }}

    QFrame#StatCard[status="success"]{{
    border:2px solid #2ECC71;
    }}

    QFrame#StatCard[status="warning"]{{
    border:2px solid #F1C40F;
    }}

    QFrame#StatCard[status="danger"]{{
    border:2px solid #E74C3C;
    }}

    QLabel#StatCardIcon{{
    color:white;
    }}

    QLabel#StatCardTitle{{
    color:#B8B8B8;
    font-size:13px;
    font-weight:500;
    }}

    QLabel#StatCardValue{{
    color:white;
    font-size:30px;
    font-weight:bold;
    }}

    QLabel#StatCardUnit{{
    color:#8E8E8E;
    font-size:12px;
    }}
    """