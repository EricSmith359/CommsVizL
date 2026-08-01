# commsvizl

A **tiny pandas visualization library** with a **dark, flat dashboard theme**
inspired by games-as-a-service (GaaS) ops dashboards. Two small namespaces,
functions short enough to read in a glance, and a theme that's applied the
moment you import it. Every function takes a pandas `DataFrame` and returns a
matplotlib `Axes`.

## Install

```bash
pip install -e .
```

Dependencies: `pandas` and `matplotlib`.

## Quickstart

```python
import pandas as pd
from commsvizl import plot, summarize  # importing applies the dark theme

dau = pd.read_csv("data/raw/dau_daily.csv", index_col="day")
revenue = pd.read_csv("data/raw/revenue_weekly.csv", index_col="week")
retention = pd.read_csv("data/raw/retention_cohorts.csv", index_col="cohort")

plot.area(dau, alpha=0.22)                      # DAU trend
plot.bar(revenue, stacked=True)                 # weekly revenue by segment
plot.heatmap(retention, fmt="{:.0f}%")          # retention cohort grid
summarize.kpi(dau, "dau", label="Daily active users")  # dark KPI card
```

Or run the ready-made demo, which writes every chart to `reports/figures/`:

```bash
python notebooks/quickstart.py
```

## API

### `plot` — chart the numeric columns

| Call | What it draws |
| --- | --- |
| `plot.line(df)` | line chart |
| `plot.bar(df)` | bar chart |
| `plot.stacked(df)` | stacked bar chart (one bar per row) |
| `plot.area(df)` | stacked area chart |
| `plot.hist(df, bins=20)` | overlaid histogram |
| `plot.box(df)` | box-and-whisker plot |
| `plot.scatter(df, x, y)` | scatter of `x` vs `y` |
| `plot.heatmap(df, fmt="{:.0f}")` | magnitude heatmap of a matrix, annotated per cell |

### `summarize` — chart the shape of the frame

| Call | What it draws |
| --- | --- |
| `summarize.df(df)` | bar chart of `describe()` stats |
| `summarize.missing(df)` | missing-value count per column |
| `summarize.counts(df, column)` | value counts for one column |
| `summarize.dtypes(df)` | pie chart of column dtypes |
| `summarize.kpi(df, column)` | dark KPI card: latest value + % change vs previous |

Any extra keyword arguments pass straight through to pandas' `.plot()`, so
`plot.line(df, title="Trend", figsize=(8, 4))` works as expected.

Pass anything that isn't a `DataFrame` and you get a clear `TypeError` —
this library is pandas-only by design.

## Theme

The dark, flat theme is applied automatically on `import commsvizl`. Colors
live in `commsvizl.theme` and follow the dashboard palette:

| Role | Color |
| --- | --- |
| Categorical 1 | `#2E6FE8` (blue) |
| Categorical 2 | `#E8632E` (orange) |
| Categorical 3 | `#1FA971` (green) |
| Positive delta | `#34B364` |
| Negative delta | `#E4564C` |
| Page / chart background | `#20242B` (charcoal) |
| KPI card panel | `#2A2F37` |

```python
from commsvizl import theme
theme.apply()          # re-apply if another library changed matplotlib's settings
theme.PALETTE          # the categorical color cycle
```

Fonts prefer `Inter` / `Helvetica Neue` and fall back to matplotlib's built-in
`DejaVu Sans`, so charts render cleanly even if those fonts aren't installed.

## Sample data

Three small games-as-a-service datasets in `data/raw/`, one per dashboard
panel:

- **`dau_daily.csv`** — daily active users over 30 days (with a couple of
  live-event spikes).
- **`revenue_weekly.csv`** — weekly revenue split by monetization segment
  (battle pass / cosmetics / currency packs).
- **`revenue_by_region.csv`** — the same weekly revenue split by region
  (NA / SA / Europe / Asia).
- **`retention_cohorts.csv`** — retention by weekly cohort (D1–D30); recent
  cohorts have empty cells for days that haven't elapsed yet.

`python notebooks/quickstart.py` turns these into the dashboard panels
(KPI cards, DAU trend, stacked revenue bar, retention heatmap).

## Project layout

```
├── data/              # raw, interim, processed, external
├── notebooks/         # exploration only
├── src/commsvizl/     # the importable package
├── models/            # trained artifacts
├── reports/figures/   # graphics for write-ups
├── docs/              # mkdocs site
└── pyproject.toml     # project metadata
```

## License

[MIT](LICENSE) — free for all to use and edit.
