"""commsvizl — a tiny pandas visualization library.

A dark, flat theme (matching a games-as-a-service ops dashboard) plus two
small namespaces built on pandas' own plotting:

    >>> from commsvizl import plot, summarize
    >>> plot.line(df)          # line chart of numeric columns
    >>> plot.heatmap(matrix)   # magnitude heatmap (e.g. a cohort grid)
    >>> summarize.df(df)       # bar chart of describe() stats
    >>> summarize.kpi(df, "dau")  # dark KPI card with % change

The theme is applied on import; call ``commsvizl.theme.apply()`` to re-apply
it. Every function takes a pandas ``DataFrame`` and returns a matplotlib
``Axes`` so you can keep styling, saving, or showing it as usual.
"""

from commsvizl import theme

theme.apply()

from commsvizl import plot, summarize

__all__ = ["plot", "summarize", "theme"]
__version__ = "0.2.0"
