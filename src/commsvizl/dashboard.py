"""High-level GaaS dashboard: one method per named chart.

Point it at the folder holding the sample CSVs and call a chart by name —
each method builds the styled chart, shows it on screen, and returns its
matplotlib ``Axes``:

    >>> from commsvizl import Dashboard
    >>> gaas = Dashboard("data/raw")
    >>> gaas.dau_chart()             # daily active users trend
    >>> gaas.revenue_by_segment()    # weekly revenue by segment
    >>> gaas.kpi_row()               # four KPI tiles
"""

import matplotlib.pyplot as plt
import pandas as pd

from commsvizl import plot, summarize, theme

_SEGMENTS = {"battle_pass": "Battle pass", "cosmetics": "Cosmetics",
             "currency_packs": "Currency packs"}


class Dashboard:
    """Load the GaaS sample CSVs from ``data_dir`` and chart them by name."""

    def __init__(self, data_dir="data/raw"):
        self.data_dir = data_dir

    def _read(self, name, index):
        return pd.read_csv(f"{self.data_dir}/{name}", index_col=index)

    def dau_chart(self):
        """Daily active users: filled trend with a crisp line."""
        dau = self._read("dau_daily.csv", "day")
        ax = plot.area(dau, alpha=0.22, legend=False)
        plot.line(dau, ax=ax, linewidth=2.5, legend=False, color=theme.BLUE)
        ax.grid(False)
        ax.set_ylim(150000, 219000)
        ax.set_title("Daily active users")
        return _show(ax)

    def revenue_by_segment(self):
        """Weekly revenue stacked by monetization segment."""
        return _show(self._revenue("revenue_weekly.csv", "by segment", _SEGMENTS))

    def revenue_by_region(self):
        """Weekly revenue stacked by region."""
        return _show(self._revenue("revenue_by_region.csv", "by region", {}))

    def _revenue(self, name, subtitle, rename):
        rev = self._read(name, "week").rename(columns=rename)
        rev.index = rev.index.str.replace("Wk", "", regex=False)
        ax = plot.stacked(rev, rot=0)
        ax.grid(False)
        ax.legend(prop={"weight": "bold"}, labelcolor=theme.MUTED)
        ax.set_xlabel("Week")
        ax.set_title(f"Weekly revenue {subtitle}")
        return ax

    def retention_heatmap(self):
        """Retention rate by weekly cohort (D1-D30)."""
        ax = plot.heatmap(self._read("retention_cohorts.csv", "cohort"), fmt="{:.0f}%")
        ax.set_title("Retention by cohort")
        return _show(ax)

    def kpi_row(self):
        """Four KPI tiles, each with its week-over-week change."""
        k = self._read("weekly_kpis.csv", "week")
        fig, cards = plt.subplots(1, 4, figsize=(16, 3.0))
        fig.patch.set_facecolor(theme.PAGE)
        fig.subplots_adjust(wspace=0.15)
        summarize.kpi(k, "dau", label="Daily active users", since="last week", ax=cards[0])
        summarize.kpi(k, "d7_retention", fmt="{:.0f}%", label="D7 retention", since="last week", ax=cards[1])
        summarize.kpi(k, "arpu", fmt="${:.2f}", label="ARPU (30d)", since="last week", ax=cards[2])
        summarize.kpi(k, "mtd_revenue", fmt="${:,.0f}", label="MTD revenue", since="last week", ax=cards[3])
        return _show(cards[0])


def _show(ax):
    """Display the figure on screen and return the Axes."""
    plt.show()
    return ax
