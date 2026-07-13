from PySide6.QtWidgets import (
    QWizardPage,
    QLabel,
    QLineEdit,
    QFormLayout,
    QVBoxLayout,
    QGroupBox
)
from PySide6.QtWidgets import QMessageBox


class ClientPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.setTitle("Información del Cliente")
        self.setSubTitle(
            "Ingrese la información básica del cliente."
        )

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        group = QGroupBox("Cliente")

        form = QFormLayout()

        self.company_edit = QLineEdit()
        self.company_edit.setPlaceholderText("Empresa")

        self.contact_edit = QLineEdit()
        self.contact_edit.setPlaceholderText("Nombre del contacto")

        self.email_edit = QLineEdit()
        self.email_edit.setPlaceholderText("correo@empresa.com")

        self.phone_edit = QLineEdit()
        self.phone_edit.setPlaceholderText("Teléfono")

        form.addRow(QLabel("Empresa:"), self.company_edit)
        form.addRow(QLabel("Contacto:"), self.contact_edit)
        form.addRow(QLabel("Correo:"), self.email_edit)
        form.addRow(QLabel("Teléfono:"), self.phone_edit)

        group.setLayout(form)

        layout.addWidget(group)
        layout.addStretch()

    def validatePage(self):

        print("1. Entró a validatePage")

        try:
            company = self.company_edit.text().strip()
            print("2. Empresa:", company)

            form = self.wizard().study_form
            print("3. StudyForm encontrado")

            form.company = company
            form.contact = self.contact_edit.text().strip()
            form.email = self.email_edit.text().strip()
            form.phone = self.phone_edit.text().strip()

            print("4. Datos guardados")

            return True

        except Exception as e:
         print("ERROR:", e)
         return False