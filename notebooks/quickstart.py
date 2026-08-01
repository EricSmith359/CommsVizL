"""Quickstart: rebuild the GaaS ops dashboard with commsvizl.

Run from the repository root:

    python notebooks/quickstart.py

It reads the three sample CSVs in data/raw/ and saves the dashboard panels
into reports/figures/ so you can open them and confirm everything works.
"""

import matplotlib

matplotlib.use("Agg")  # save to files without needing a display
import matplotlib.pyplot as plt
import pandas as pd

from commsvizl import plot, summarize, theme  # importing applies the dark theme


def save(ax, name):
    ax.figure.savefig(f"reports/figures/{name}.png", bbox_inches="tight", dpi=120)
    plt.close(ax.figure)
    print(f"  wrote reports/figures/{name}.png")


# --- data -----------------------------------------------------------------
dau = pd.read_csv("data/raw/dau_daily.csv", index_col="day")
revenue = pd.read_csv("data/raw/revenue_weekly.csv", index_col="week")
retention = pd.read_csv("data/raw/retention_cohorts.csv", index_col="cohort")
kpis = pd.read_csv("data/raw/weekly_kpis.csv", index_col="week")

# --- KPI row: four tiles, each with its week-over-week change --------------
fig, cards = plt.subplots(1, 4, figsize=(16, 3.0))
fig.patch.set_facecolor(theme.PAGE)
fig.subplots_adjust(wspace=0.15)
summarize.kpi(kpis, "dau", label="Daily active users", since="last week", ax=cards[0])
summarize.kpi(kpis, "d7_retention", fmt="{:.0f}%", label="D7 retention",
              since="last week", ax=cards[1])
summarize.kpi(kpis, "arpu", fmt="${:.2f}", label="ARPU (30d)",
              since="last week", ax=cards[2])
summarize.kpi(kpis, "mtd_revenue", fmt="${:,.0f}", label="MTD revenue",
              since="last week", ax=cards[3])
save(cards[0], "kpi_row")

# --- DAU trend (light fill + strong line, single series) ------------------
ax = plot.area(dau, alpha=0.22, legend=False)
plot.line(dau, ax=ax, linewidth=2.5, legend=False, color=theme.BLUE)
ax.grid(False)                 # no gridlines on the trend
ax.set_ylim(150000, 219000)    # symmetric padding centers the trend line
ax.set_title("Daily active users")
save(ax, "dau_trend")

# --- weekly revenue by monetization segment (stacked bar) -----------------
segments = {"battle_pass": "Battle pass", "cosmetics": "Cosmetics",
            "currency_packs": "Currency packs"}
rev = revenue.rename(columns=segments)
rev.index = rev.index.str.replace("Wk", "", regex=False)  # "Wk1" -> "1"
ax = plot.bar(rev, stacked=True, rot=0)                    # horizontal tick labels
ax.legend(prop={"weight": "semibold"}, labelcolor=theme.MUTED)  # cleaner labels
ax.set_xlabel("Week")
ax.set_title("Weekly revenue by segment")
save(ax, "revenue_by_segment")

# --- weekly revenue by region (stacked bar) -------------------------------
region = pd.read_csv("data/raw/revenue_by_region.csv", index_col="week")
region.index = region.index.str.replace("Wk", "", regex=False)
ax = plot.stacked(region, rot=0)
ax.legend(prop={"weight": "semibold"}, labelcolor=theme.MUTED)
ax.set_xlabel("Week")
ax.set_title("Weekly revenue by region")
save(ax, "revenue_by_region")

# --- retention cohort heatmap (empty recent cells left blank) -------------
ax = plot.heatmap(retention, fmt="{:.0f}%")
ax.set_title("Retention by cohort")
save(ax, "retention_heatmap")

print("Done. Open the PNGs in reports/figures/ to see the dashboard.")
