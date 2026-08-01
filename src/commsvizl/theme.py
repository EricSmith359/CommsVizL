"""Dark, flat theme matching the GaaS ops-dashboard aesthetic.

Applied automatically on ``import commsvizl``. Call :func:`apply` to
re-apply it (e.g. after another library changes matplotlib's settings).
"""

import os

import matplotlib as mpl
from cycler import cycler
from matplotlib import font_manager

# preferred fonts, best first; only the installed ones are used (no warnings)
_FONTS = ["Inter", "Helvetica Neue", "Arial", "DejaVu Sans"]

# Inter ships with the package (SIL OFL, see fonts/Inter-OFL.txt)
_FONT_DIR = os.path.join(os.path.dirname(__file__), "fonts")

# categorical palette — blue / orange / green, then extras for >3 series
PALETTE = ["#2E6FE8", "#E8632E", "#1FA971", "#7E57F0", "#E8B72E", "#17B0C4"]
BLUE, ORANGE, GREEN = PALETTE[0], PALETTE[1], PALETTE[2]

# surfaces & ink (flat: plot area matches the page)
PAGE = "#20242B"      # figure / axes background (soft charcoal)
CARD = "#2A2F37"      # KPI card panel, a touch lighter than the page
GRID = "#363C44"      # subtle horizontal gridlines
INK = "#F2F4F7"       # primary text
MUTED = "#9AA1AA"     # labels, ticks, legend

# semantic deltas
POSITIVE = "#34B364"
NEGATIVE = "#E4564C"

_RC = {
    "figure.facecolor": PAGE,
    "savefig.facecolor": PAGE,
    "axes.facecolor": PAGE,
    "axes.edgecolor": GRID,
    "axes.labelcolor": MUTED,
    "axes.titlecolor": INK,
    "axes.titleweight": "bold",
    "axes.titlesize": 14,
    "axes.titlelocation": "left",
    "axes.grid": True,
    "axes.grid.axis": "y",
    "axes.axisbelow": True,
    "axes.spines.top": False,
    "axes.spines.right": False,
    "grid.color": GRID,
    "grid.linewidth": 0.8,
    "xtick.color": MUTED,
    "ytick.color": MUTED,
    "text.color": INK,
    "legend.frameon": False,
    "legend.labelcolor": MUTED,
    "figure.figsize": (8.0, 4.5),
}


def _register_bundled_fonts():
    """Register the packaged Inter fonts with matplotlib (once)."""
    have = {f.name for f in font_manager.fontManager.ttflist}
    if "Inter" in have or not os.path.isdir(_FONT_DIR):
        return
    for name in os.listdir(_FONT_DIR):
        if name.lower().endswith((".ttf", ".otf")):
            font_manager.fontManager.addfont(os.path.join(_FONT_DIR, name))


def _installed_fonts():
    """Return the preferred fonts that are actually installed (never empty)."""
    have = {f.name for f in font_manager.fontManager.ttflist}
    return [name for name in _FONTS if name in have] or ["DejaVu Sans"]


def apply():
    """Apply the commsvizl dark theme to matplotlib globally."""
    _register_bundled_fonts()
    mpl.rcParams["axes.prop_cycle"] = cycler(color=PALETTE)
    mpl.rcParams["font.family"] = _installed_fonts()
    for key, value in _RC.items():
        if key in mpl.rcParams:
            mpl.rcParams[key] = value
