# commsvizl

A tiny pandas visualization library — one dependency, two small namespaces.

```python
from commsvizl import plot, summarize

plot.line(df)
summarize.df(df)
```

## `plot`

- `plot.line(df)` — line chart of numeric columns
- `plot.bar(df)` — bar chart of numeric columns
- `plot.area(df)` — stacked area chart
- `plot.hist(df, bins=20)` — overlaid histogram
- `plot.box(df)` — box-and-whisker plot
- `plot.scatter(df, x, y)` — scatter of `x` vs `y`

## `summarize`

- `summarize.df(df)` — bar chart of `describe()` stats
- `summarize.missing(df)` — missing-value count per column
- `summarize.counts(df, column)` — value counts for one column
- `summarize.dtypes(df)` — pie chart of column dtypes

Every function takes a pandas `DataFrame` and returns a matplotlib `Axes`.
Extra keyword arguments pass straight through to pandas' `.plot()`.
