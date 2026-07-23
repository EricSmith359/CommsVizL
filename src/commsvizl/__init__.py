"""commsvizl — a tiny pandas visualization library.

Two small namespaces, both built on pandas' own plotting:

    >>> from commsvizl import plot, summarize
    >>> plot.line(df)        # line chart of numeric columns
    >>> summarize.df(df)     # bar chart of describe() stats

Every function takes a pandas ``DataFrame`` and returns a matplotlib
``Axes`` so you can keep styling, saving, or showing it as usual.
"""

from commsvizl import plot, summarize

__all__ = ["plot", "summarize"]
__version__ = "0.1.0"
