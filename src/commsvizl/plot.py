"""Quick charts of a DataFrame's numeric columns.

    >>> from commsvizl import plot
    >>> plot.line(df)
    >>> plot.scatter(df, x="height", y="weight")
"""

from commsvizl._guard import frames_only


@frames_only
def line(df, **kw):
    """Line chart of every numeric column."""
    return df.select_dtypes("number").plot(kind="line", **kw)


@frames_only
def bar(df, **kw):
    """Bar chart of every numeric column."""
    return df.select_dtypes("number").plot(kind="bar", **kw)


@frames_only
def area(df, **kw):
    """Stacked area chart of every numeric column."""
    return df.select_dtypes("number").plot(kind="area", **kw)


@frames_only
def hist(df, bins=20, **kw):
    """Overlaid histogram of every numeric column."""
    return df.select_dtypes("number").plot(kind="hist", bins=bins, alpha=0.6, **kw)


@frames_only
def box(df, **kw):
    """Box-and-whisker plot of every numeric column."""
    return df.select_dtypes("number").plot(kind="box", **kw)


@frames_only
def scatter(df, x, y, **kw):
    """Scatter plot of column ``x`` against column ``y``."""
    return df.plot(kind="scatter", x=x, y=y, **kw)
