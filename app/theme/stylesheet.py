from app.theme.colors import Colors


def load_stylesheet():

    return f"""

    QWidget {{
        background-color: {Colors.BACKGROUND};
        color: {Colors.LIGHT};
        font-family: Segoe UI;
        font-size: 10pt;
    }}

    QPushButton#menuButton{{
    background-color:#242424;
    color:white;
    border:1px solid #343434;
    border-radius:10px;
    padding:10px;
    font-weight:bold;
    }}

    QPushButton:hover {{
        background-color: #42A5F5;
    }}

    QPushButton:pressed {{
        background-color: #1565C0;
    }}

    QPushButton#menuActive{{
    background-color:#1976D2;
    color:white;
    border-radius:10px;
    padding:10px;
    font-weight:bold;
    }}

    QFrame#StatCard{{

    background-color:#242424;
    border:1px solid #343434;
    border-radius:10px;
    }}

    QFrame#StatCard[status="success"]{{
    border:1px solid #2ECC71;
    }}

    QFrame#StatCard[status="warning"]{{
    border:1px solid #F1C40F;
    }}

    QFrame#StatCard[status="danger"]{{
    border:1px solid #E74C3C;
    }}

    QLabel#StatCardIcon{{
    color:white;
    }}

    QLabel#StatCardTitle{{
    color:#C7C7C7;
    font-size:12px;
    font-weight:400;
    }}

    QLabel#StatCardValue{{
    color:white;
    font-size:15px;
    font-weight:700;
    }}
    
    QLabel#StatCardIcon,
    QLabel#StatCardTitle,
    QLabel#StatCardValue{{
    background-color: transparent;
    }}
    """