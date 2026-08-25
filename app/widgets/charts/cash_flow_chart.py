from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter


class CashFlowChart(FigureCanvasQTAgg):

    def __init__(self, result):

        self.result = result

        self.figure = Figure(figsize=(8, 4))

        super().__init__(self.figure)

        self.setMinimumHeight(350)
        self.setMinimumWidth(600)

        self.axes = self.figure.add_subplot(111)

        self.draw_chart()

    def draw_chart(self):

        # =================================================
        # DATOS
        # =================================================

        # El motor conserva los 25 años completos.
        cash_flows = self.result.cash_flows

        # Flujo acumulado completo
        cumulative_full = []

        total = 0

        for cash_flow in cash_flows:

            total += cash_flow

            cumulative_full.append(total)

        # =================================================
        # DATOS MOSTRADOS EN EL GRÁFICO
        # =================================================

        # Mostramos únicamente los primeros 8 puntos:
        # Año 0 hasta Año 7

        display_count = min(
            8,
            len(cumulative_full)
        )

        cumulative = cumulative_full[
            :display_count
        ]

        years = list(
            range(len(cumulative))
        )

        print(
            "CUMULATIVE COMPLETO:",
            cumulative_full
        )

        print(
            "CUMULATIVE MOSTRADO:",
            cumulative
        )

        print(
            "MIN MOSTRADO:",
            min(cumulative)
        )

        print(
            "MAX MOSTRADO:",
            max(cumulative)
        )

        # =================================================
        # ESCALA DEL GRÁFICO
        # =================================================

        minimum = min(cumulative)

        maximum = max(cumulative)

        # Margen visual

        data_range = maximum - minimum

        if data_range == 0:

            data_range = 1

        margin = data_range * 0.10

        self.axes.set_ylim(
            minimum - margin,
            maximum + margin
        )

        # =================================================
        # EJE X
        # =================================================

        self.axes.set_xticks(
            years
        )

        # =================================================
        # BUSCAR PAYBACK
        # =================================================

        crossing_year = None

        for i in range(
            1,
            len(cumulative)
        ):

            previous_value = (
                cumulative[i - 1]
            )

            current_value = (
                cumulative[i]
            )

            if (
                previous_value < 0
                and current_value >= 0
            ):

                # Interpolación lineal
                fraction = (
                    -previous_value
                    /
                    (
                        current_value
                        - previous_value
                    )
                )

                crossing_year = (
                    years[i - 1]
                    + fraction
                )

                break

        # =================================================
        # LÍNEA DE EQUILIBRIO
        # =================================================

        self.axes.axhline(
            0,
            color="#888888",
            linestyle="--",
            linewidth=1,
            zorder=2
        )

        # =================================================
        # INVERSIÓN INICIAL
        # =================================================

        initial_investment = (
            cumulative[0]
        )

        self.axes.axhline(
            initial_investment,
            color="#E74C3C",
            linestyle=":",
            linewidth=1,
            alpha=0.7,
            zorder=2
        )

        # Etiqueta de inversión

        self.axes.text(

            0.15,

            initial_investment
            - data_range * 0.04,

            f"Inversión: "
            f"${abs(initial_investment) / 1_000_000:,.1f} M",

            color="#E74C3C",

            fontsize=8,

            ha="left",

            va="top",

            zorder=7
        )

        # =================================================
        # ÁREA NEGATIVA
        # =================================================

        self.axes.fill_between(

            years,

            cumulative,

            0,

            where=[
                value < 0
                for value in cumulative
            ],

            color="#E74C3C",

            alpha=0.20,

            interpolate=True
        )

        # =================================================
        # ÁREA POSITIVA
        # =================================================

        self.axes.fill_between(

            years,

            cumulative,

            0,

            where=[
                value >= 0
                for value in cumulative
            ],

            color="#4CAF50",

            alpha=0.15,

            interpolate=True
        )

        # =================================================
        # LÍNEA ROJA Y VERDE
        # =================================================

        if crossing_year is not None:

            # ---------------------------------------------
            # PARTE ROJA
            # ---------------------------------------------

            red_years = []

            red_values = []

            for year, value in zip(
                years,
                cumulative
            ):

                if year < crossing_year:

                    red_years.append(
                        year
                    )

                    red_values.append(
                        value
                    )

            # Agregar punto exacto de recuperación

            red_years.append(
                crossing_year
            )

            red_values.append(
                0
            )

            self.axes.plot(

                red_years,

                red_values,

                marker="o",

                linewidth=2.5,

                markersize=4,

                color="#E74C3C",

                zorder=4
            )

            # ---------------------------------------------
            # PARTE VERDE
            # ---------------------------------------------

            green_years = [
                crossing_year
            ]

            green_values = [
                0
            ]

            for year, value in zip(
                years,
                cumulative
            ):

                if year > crossing_year:

                    green_years.append(
                        year
                    )

                    green_values.append(
                        value
                    )

            self.axes.plot(

                green_years,

                green_values,

                marker="o",

                linewidth=2.5,

                markersize=4,

                color="#4CAF50",

                zorder=4
            )

            # ---------------------------------------------
            # PUNTO EXACTO DEL PAYBACK
            # ---------------------------------------------

            self.axes.scatter(

                [crossing_year],

                [0],

                s=90,

                color="#4CAF50",

                edgecolor="#1E1E1E",

                linewidth=1.5,

                zorder=6
            )

            # ---------------------------------------------
            # LÍNEA VERTICAL DEL PAYBACK
            # ---------------------------------------------

            self.axes.axvline(

                crossing_year,

                color="#4CAF50",

                linestyle="--",

                linewidth=1.5,

                alpha=0.8,

                zorder=2
            )

            # ---------------------------------------------
            # ETIQUETA DEL PAYBACK
            # ---------------------------------------------

            label_y = (
                maximum
                - data_range * 0.15
            )

            self.axes.annotate(

                f"Recuperación de la inversión\n"
                f"{crossing_year:.1f} años",

                xy=(

                    crossing_year,

                    0
                ),

                xytext=(

                    crossing_year + 0.5,

                    label_y
                ),

                color="white",

                fontsize=9,

                ha="left",

                va="center",

                bbox=dict(

                    boxstyle="round,pad=0.6",

                    facecolor="#1E1E1E",

                    edgecolor="#4CAF50",

                    linewidth=1.2
                ),

                arrowprops=dict(

                    arrowstyle="->",

                    color="#4CAF50",

                    linewidth=1.5,

                    shrinkA=5,

                    shrinkB=5
                ),

                zorder=8
            )

        else:

            # =================================================
            # SI NO HAY RECUPERACIÓN
            # =================================================

            self.axes.plot(

                years,

                cumulative,

                marker="o",

                linewidth=2.5,

                markersize=4,

                color="#E74C3C",

                zorder=4
            )

        # =================================================
        # FORMATO DE VALORES
        # =================================================

        self.axes.yaxis.set_major_formatter(

            FuncFormatter(

                lambda x, pos:

                f"${x / 1_000_000:,.0f} M"
            )
        )

        # =================================================
        # TÍTULOS
        # =================================================

        self.axes.set_xlabel(
            "Años",
            color="white"
        )

        self.axes.set_ylabel(
            "Flujo acumulado",
            color="white"
        )

        self.axes.set_title(
            "Flujo de caja acumulado — primeros 7 años",
            color="white"
        )

        # =================================================
        # ESTILO
        # =================================================

        self.axes.set_facecolor(
            "#1E1E1E"
        )

        self.figure.set_facecolor(
            "#1E1E1E"
        )

        self.axes.tick_params(
            colors="white"
        )

        # Bordes

        self.axes.spines[
            "top"
        ].set_visible(False)

        self.axes.spines[
            "right"
        ].set_visible(False)

        self.axes.spines[
            "left"
        ].set_color(
            "#666666"
        )

        self.axes.spines[
            "bottom"
        ].set_color(
            "#666666"
        )

        # Grid

        self.axes.grid(

            axis="y",

            linestyle="--",

            alpha=0.3,

            color="#888888"
        )

        # =================================================
        # AJUSTE FINAL
        # =================================================

        self.figure.tight_layout()