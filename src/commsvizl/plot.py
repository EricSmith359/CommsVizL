"""Quick charts of a DataFrame's numeric columns, in the commsvizl theme.

    >>> from commsvizl import plot
    >>> plot.line(df)
    >>> plot.scatter(df, x="dau", y="revenue_usd")
    >>> plot.heatmap(cohort_matrix)
"""

import matplotlib.pyplot as plt
from matplotlib.colors import LinearSegmentedColormap

from commsvizl import theme
from commsvizl._guard import frames_only

# sequential blue ramp: low values light, high values dark (cohort-grid look)
_CMAP = LinearSegmentedColormap.from_list(
    "commsvizl_seq", ["#EAF1FC", theme.BLUE, "#0F2A5A"]
)
_CMAP.set_bad(theme.PAGE)  # empty cells blend into the page


@frames_only
def line(df, **kw):
    """Line chart of every numeric column."""
    return df.select_dtypes("number").plot(kind="line", **kw)


@frames_only
def bar(df, **kw):
    """Bar chart of every numeric column."""
    return df.select_dtypes("number").plot(kind="bar", **kw)


@frames_only
def stacked(df, **kw):
    """Stacked bar chart of every numeric column (one bar per row)."""
    return df.select_dtypes("number").plot(kind="bar", stacked=True, **kw)


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
    return df.plot(kind="scatter", x=x, y=y, color=theme.BLUE, **kw)


@frames_only
def heatmap(df, fmt="{:.0f}", **kw):
    """Magnitude heatmap of the numeric columns, annotated per cell."""
    num = df.select_dtypes("number")
    lo, hi = num.min().min(), num.max().max()
    ax = plt.gca()
    ax.grid(False)
    ax.imshow(num.values, aspect="auto", cmap=_CMAP, **kw)
    ax.set_xticks(range(len(num.columns)), list(num.columns))
    ax.set_yticks(range(len(num.index)), list(num.index))
    for i, row in enumerate(num.values):
        for j, v in enumerate(row):
            if v == v:  # skip NaN
                strong = hi > lo and (v - lo) / (hi - lo) > 0.5
                ax.text(j, i, fmt.format(v), ha="center", va="center",
                        color="white" if strong else "#0F2A5A", fontsize=9)
    return ax
