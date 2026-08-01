"""Charts that summarize the shape of a DataFrame, in the commsvizl theme.

    >>> from commsvizl import summarize
    >>> summarize.df(df)
    >>> summarize.missing(df)
    >>> summarize.counts(df, "platform")
    >>> summarize.kpi(df, "dau")
"""

import matplotlib.pyplot as plt

from commsvizl import theme
from commsvizl._guard import frames_only


@frames_only
def df(data, **kw):
    """Bar chart of ``describe()`` statistics per numeric column."""
    return data.describe().T.plot(kind="bar", **kw)


@frames_only
def missing(data, **kw):
    """Bar chart of the missing-value count per column."""
    return data.isna().sum().plot(kind="bar", **kw)


@frames_only
def counts(data, column, **kw):
    """Bar chart of value counts for a single column."""
    return data[column].value_counts().plot(kind="bar", **kw)


@frames_only
def dtypes(data, **kw):
    """Pie chart of how many columns share each dtype."""
    return data.dtypes.astype(str).value_counts().plot(kind="pie", **kw)


@frames_only
def kpi(data, column, fmt="{:,.0f}", label=None, since="prev", ax=None):
    """Dark KPI card: the latest value of a column and its % change."""
    series = data[column].dropna()
    value = series.iloc[-1]
    prev = series.iloc[-2] if len(series) > 1 else value
    delta = (value - prev) / prev * 100 if prev else 0.0
    return _card(ax or plt.gca(), label or column, fmt.format(value), delta, since)


def _card(ax, label, value, delta, since="prev"):
    """Render ``ax`` as a dashboard KPI tile and return it."""
    ax.set_facecolor(theme.CARD)
    ax.set_xticks([])
    ax.set_yticks([])
    for spine in ax.spines.values():
        spine.set_visible(False)
    color = theme.POSITIVE if delta >= 0 else theme.NEGATIVE
    sign = "+" if delta >= 0 else ""
    ax.text(0.08, 0.72, label, color=theme.MUTED, fontsize=12, transform=ax.transAxes)
    ax.text(0.08, 0.40, value, color=theme.INK, fontsize=26,
            fontweight="bold", transform=ax.transAxes)
    ax.text(0.08, 0.16, f"{sign}{delta:.1f}% vs {since}", color=color,
            fontsize=11, transform=ax.transAxes)
    return ax
