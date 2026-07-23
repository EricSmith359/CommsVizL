# commsvizl

A **tiny pandas visualization library**. One dependency (`pandas`), two small
namespaces, and functions short enough to read in a glance. Every function
takes a pandas `DataFrame` and returns a matplotlib `Axes`.

## Install

```bash
pip install -e .
```

> `commsvizl` draws through pandas' built-in `.plot()`, which renders with
> matplotlib. Pandas pulls matplotlib in the first time you make a chart.

## Quickstart

```python
import pandas as pd
from commsvizl import plot, summarize

df = pd.DataFrame({
    "height": [150, 160, 170, 180],
    "weight": [50, 62, 71, 85],
    "team":   ["a", "b", "a", "b"],
})

plot.line(df)                       # line chart of numeric columns
plot.scatter(df, x="height", y="weight")
summarize.df(df)                    # bar chart of describe() stats
summarize.counts(df, "team")        # value counts for one column
```

## API

### `plot` — chart the numeric columns

| Call | What it draws |
| --- | --- |
| `plot.line(df)` | line chart |
| `plot.bar(df)` | bar chart |
| `plot.area(df)` | stacked area chart |
| `plot.hist(df, bins=20)` | overlaid histogram |
| `plot.box(df)` | box-and-whisker plot |
| `plot.scatter(df, x, y)` | scatter of `x` vs `y` |

### `summarize` — chart the shape of the frame

| Call | What it draws |
| --- | --- |
| `summarize.df(df)` | bar chart of `describe()` stats |
| `summarize.missing(df)` | missing-value count per column |
| `summarize.counts(df, column)` | value counts for one column |
| `summarize.dtypes(df)` | pie chart of column dtypes |

Any extra keyword arguments pass straight through to pandas' `.plot()`, so
`plot.line(df, title="Trend", figsize=(8, 4))` works as expected.

Pass anything that isn't a `DataFrame` and you get a clear `TypeError` —
this library is pandas-only by design.

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
