# commsvizl

A tiny pandas visualization library with a dark, flat dashboard theme
(inspired by games-as-a-service ops dashboards). The theme is applied on
`import commsvizl`.

```python
from commsvizl import plot, summarize

plot.line(df)
plot.heatmap(matrix)
summarize.df(df)
summarize.kpi(df, "dau")
```

## `plot`

- `plot.line(df)` — line chart of numeric columns
- `plot.bar(df)` — bar chart of numeric columns
- `plot.area(df)` — stacked area chart
- `plot.hist(df, bins=20)` — overlaid histogram
- `plot.box(df)` — box-and-whisker plot
- `plot.scatter(df, x, y)` — scatter of `x` vs `y`
- `plot.heatmap(df, fmt="{:.0f}")` — magnitude heatmap of a matrix, annotated per cell

## `summarize`

- `summarize.df(df)` — bar chart of `describe()` stats
- `summarize.missing(df)` — missing-value count per column
- `summarize.counts(df, column)` — value counts for one column
- `summarize.dtypes(df)` — pie chart of column dtypes
- `summarize.kpi(df, column)` — dark KPI card: latest value + % change vs previous

Every function takes a pandas `DataFrame` and returns a matplotlib `Axes`.
Extra keyword arguments pass straight through to pandas' `.plot()`.

## Theme

Colors live in `commsvizl.theme` (`PALETTE`, `BLUE`, `ORANGE`, `GREEN`,
`POSITIVE`, `NEGATIVE`, ...). Call `theme.apply()` to re-apply the dark theme
if another library changes matplotlib's settings.
