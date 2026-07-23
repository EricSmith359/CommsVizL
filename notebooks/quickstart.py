"""Quickstart: try commsvizl on the shipped sample dataset.

Run from the repository root:

    python notebooks/quickstart.py

It reads data/raw/sample_sales.csv and saves a few charts into
reports/figures/ so you can open them and confirm everything works.
"""

import matplotlib

matplotlib.use("Agg")  # save to files without needing a display
import matplotlib.pyplot as plt
import pandas as pd

from commsvizl import plot, summarize

df = pd.read_csv("data/raw/sample_sales.csv")
print("Loaded sample_sales.csv:")
print(df.head(), "\n")


def save(ax, name):
    ax.figure.savefig(f"reports/figures/{name}.png", bbox_inches="tight")
    plt.close(ax.figure)
    print(f"  wrote reports/figures/{name}.png")


save(plot.line(df), "line")
save(plot.hist(df), "hist")
save(plot.box(df), "box")
save(plot.scatter(df, x="units_sold", y="revenue"), "scatter")
save(summarize.df(df), "summary")
save(summarize.missing(df), "missing")
save(summarize.counts(df, "region"), "region_counts")
save(summarize.dtypes(df), "dtypes")
print("\nDone. Open the PNGs in reports/figures/ to see the charts.")
