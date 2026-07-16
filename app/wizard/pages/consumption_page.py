from PySide6.QtWidgets import (
    QWizardPage,
    QVBoxLayout,
    QFormLayout,
    QGroupBox,
    QLabel,
    QDoubleSpinBox,
    QMessageBox
)


class ConsumptionPage(QWizardPage):

    def __init__(self):
        super().__init__()

        self.setTitle("Información Energética")
        self.setSubTitle(
            "Ingrese los datos del consumo eléctrico."
        )

        self.build_ui()

    def build_ui(self):

        layout = QVBoxLayout(self)

        group = QGroupBox("Consumo Energético")

        form = QFormLayout()

        # Consumo mensual
        self.monthly_consumption = QDoubleSpinBox()
        self.monthly_consumption.setRange(0, 1_000_000)
        self.monthly_consumption.setDecimals(1)
        self.monthly_consumption.setSuffix(" kWh")
        self.monthly_consumption.setValue(2500)

        # Tarifa promedio
        self.average_tariff = QDoubleSpinBox()
        self.average_tariff.setRange(0, 10000)
        self.average_tariff.setDecimals(0)
        self.average_tariff.setPrefix("$ ")
        self.average_tariff.setSuffix(" COP/kWh")
        self.average_tariff.setValue(980)

        # Cobertura objetivo
        self.coverage = QDoubleSpinBox()
        self.coverage.setRange(1, 100)
        self.coverage.setDecimals(0)
        self.coverage.setSuffix(" %")
        self.coverage.setValue(90)

        form.addRow(
            QLabel("Consumo mensual:"),
            self.monthly_consumption
        )

        form.addRow(
            QLabel("Tarifa promedio:"),
            self.average_tariff
        )

        form.addRow(
            QLabel("Cobertura objetivo:"),
            self.coverage
        )

        group.setLayout(form)

        layout.addWidget(group)
        layout.addStretch()

    def validatePage(self):

        if self.monthly_consumption.value() <= 0:

            QMessageBox.warning(
                self,
                "Información incompleta",
                "Ingrese un consumo mensual mayor que cero."
            )

            self.monthly_consumption.setFocus()
            return False

        if self.average_tariff.value() <= 0:

            QMessageBox.warning(
                self,
                "Información incompleta",
                "Ingrese una tarifa promedio mayor que cero."
            )

            self.average_tariff.setFocus()
            return False

        # Guardar la información en el StudyForm
        form = self.wizard().study_form

        form.monthly_consumption_kwh = self.monthly_consumption.value()
        form.average_tariff = self.average_tariff.value()
        form.target_coverage = self.coverage.value()

        return True