"""Shared guard that keeps the library pandas-only."""

import functools

import pandas as pd


def frames_only(fn):
    """Raise ``TypeError`` unless the first argument is a DataFrame."""

    @functools.wraps(fn)
    def wrapper(data, *args, **kwargs):
        if not isinstance(data, pd.DataFrame):
            raise TypeError("commsvizl works only with pandas DataFrames")
        return fn(data, *args, **kwargs)

    return wrapper
