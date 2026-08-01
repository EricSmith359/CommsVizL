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

## Charts

Import the two namespaces once — the dark theme is applied automatically:

```python
from commsvizl import plot, summarize
```

Every function below takes a pandas `DataFrame` as its first argument and
returns a matplotlib `Axes`. The examples assume the sample data in
`data/raw/` (see [Sample data](#sample-data)).

### `plot` — chart your columns

Unless noted, these operate on **every numeric column** of the frame and plot
it against the DataFrame's index; series colors cycle blue → orange → green.

#### `plot.line(df)`
```python
plot.line(dau)
```
One line per numeric column across the index. A trend/time-series view — the
DAU-over-time shape.

#### `plot.bar(df)`
```python
plot.bar(revenue)
```
Grouped vertical bars: one cluster per row, with each numeric column drawn as
a separate bar side by side within the cluster.

#### `plot.stacked(df)`
```python
plot.stacked(revenue, rot=0)
```
Vertical bars, one per row, with each numeric column **stacked** on top of the
last so the segments sum to the bar's total. This is the weekly-revenue-by-
segment / by-region look.

#### `plot.area(df)`
```python
plot.area(dau, alpha=0.22)
```
A filled line chart — numeric columns are stacked as translucent bands from
the x-axis up. With a single column it's one filled trend (the DAU panel draws
`area` then overlays `line` for a crisp edge).

#### `plot.hist(df, bins=20)`
```python
plot.hist(dau)
```
Overlaid, semi-transparent histograms (one per numeric column) showing how
values are distributed across `bins` buckets.

#### `plot.box(df)`
```python
plot.box(revenue)
```
One box-and-whisker per numeric column: median line, interquartile box,
whiskers, and outlier points — a quick spread/outlier comparison.

#### `plot.scatter(df, x, y)`
```python
plot.scatter(df, x="dau", y="revenue")
```
A point for each row positioned by two named columns (`x`, `y`), drawn in the
theme blue. For relationships between two variables.

#### `plot.heatmap(df, fmt="{:.0f}")`
```python
plot.heatmap(retention, fmt="{:.0f}%")
```
Renders the numeric matrix as a grid of cells colored light (low) → dark blue
(high), with each value printed inside its cell (`fmt` controls formatting).
Empty/`NaN` cells blend into the background — the retention cohort grid.

### `summarize` — chart the shape of the frame

#### `summarize.df(df)`
```python
summarize.df(df)
```
Runs `describe()` and bar-charts the resulting stats (count, mean, std, min,
quartiles, max) for each numeric column.

#### `summarize.missing(df)`
```python
summarize.missing(retention)
```
One bar per column showing how many values are missing (`NaN`).

#### `summarize.counts(df, column)`
```python
summarize.counts(df, "platform")
```
Bar chart of `value_counts()` for a single column — how often each distinct
value appears.

#### `summarize.dtypes(df)`
```python
summarize.dtypes(df)
```
Pie chart of how many columns share each dtype (int, float, object, ...).

#### `summarize.kpi(df, column, label=None, since="prev", ax=None)`
```python
summarize.kpi(kpis, "dau", label="Daily active users", since="last week")
```
A single dark stat card: the big, bold **latest** value of `column`, a muted
`label` above it, and the **% change vs the previous row** below — green when
up, red when down. `since` sets the comparison wording; pass an `ax` to place
several cards on one figure as a KPI row.

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
