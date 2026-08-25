from matplotlib.backends.backend_qtagg import FigureCanvasQTAgg
from matplotlib.figure import Figure
from matplotlib.ticker import FuncFormatter


class MonthlyGenerationChart(FigureCanvasQTAgg):

    def __init__(self, result):
        self.result = result

        self.figure = Figure(figsize=(6, 3))
        super().__init__(self.figure)

        self.axes = self.figure.add_subplot(111)
        

        self.draw_chart()

    def draw_chart(self):

        months = [
            "Ene", "Feb", "Mar", "Abr",
            "May", "Jun", "Jul", "Ago",
            "Sep", "Oct", "Nov", "Dic"
        ]

        
        generation = self.result.monthly_generation

        self.axes.clear()

        bars = self.axes.bar(
        months,
        generation,
        width=0.45,          
        color="#1976D2",
        edgecolor="#42A5F5",
        linewidth=1
        )

        for bar in bars:

            height = bar.get_height()

            self.axes.text(
            bar.get_x() + bar.get_width() / 2,
            height + 30,
            f"{height:,.0f}",
            ha="center",
            va="bottom",
            fontsize=8,
            color="white"
            )

        self.axes.yaxis.set_major_formatter(
            FuncFormatter(lambda x, pos: f"{x:,.0f}")
            )
        self.axes.set_title("", color="white")
        self.axes.set_ylabel("kWh", color="white")

        self.axes.set_facecolor("#1E1E1E")
        self.figure.set_facecolor("#1E1E1E")

        self.axes.tick_params(colors="white")

        self.axes.spines["top"].set_visible(False)
        self.axes.spines["right"].set_visible(False)

        self.axes.spines["left"].set_color("#666666")
        self.axes.spines["bottom"].set_color("#666666")

        self.axes.grid(
            axis="y",
            linestyle="--",
            alpha=0.3,
            color="#888888"
        )

        self.figure.tight_layout()
        self.draw()