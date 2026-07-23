"""Charts that summarize the shape of a DataFrame.

    >>> from commsvizl import summarize
    >>> summarize.df(df)
    >>> summarize.missing(df)
    >>> summarize.counts(df, "category")
"""

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
