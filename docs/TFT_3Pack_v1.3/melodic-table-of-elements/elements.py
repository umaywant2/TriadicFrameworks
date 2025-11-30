"""Utility functions for working periodid tables of elements."""

import pandas as pd


FILEPATH = "data/periodic-table.csv"
COLUMNS_TO_KEEP = [
    "symbol",
    "period",
    "group",
    "atomic_number",
    "atomic_mass",
    "name",
    "block",
]


def read(filepath=FILEPATH, **kwargs):
    """Read the periodic table of elements.

    Arguments:
    ----------
    filepath : str, optional
        The path to the csv file. Default is FILEPATH.
    **kwargs : dict
        Additional keyword arguments to pass to pandas.read_csv.

    Returns:
    --------
    elements : Elements
        The periodic table of elements.
    """
    kwargs.setdefault("delimiter", ",")
    elements = pd.read_csv(filepath, **kwargs)
    elements = clean(elements)
    elements = move_f_block(elements)
    return elements


def clean(elements):
    """Clean the periodic table of elements.

    Arguments:
    ----------
    elements : pd.DataFrame
        The periodic table of elements.

    Returns:
    --------
    elements : pd.DataFrame
        The cleaned periodic table of elements.
    """
    # Keep only the columns we need
    elements = elements[COLUMNS_TO_KEEP]

    # Drop Uue
    elements = elements[elements["symbol"] != "Uue"]
    return elements


def move_f_block(elements):
    """Move the f-block elements to below the main table.

    Arguments:
    ----------
    elements : pd.DataFrame
        The periodic table of elements.

    Returns:
    --------
    elements : pd.DataFrame
        The periodic table of elements with the f-block elements moved.
    """
    # Change f-block group for period 6 and 7 to NaN values
    for period in [6, 7]:
        elements.loc[
            (elements["period"] == period)
            & (elements["group"] > 2)
            & (elements["block"] == "f-block"),
            "group",
        ] = pd.NA

    # Add +3 to the period number of elements wihout a group
    elements["group"] = elements["group"].fillna(0).astype(int)
    elements["period"] = elements["period"] + 3 * (elements["group"] == 0)

    # Detect continuous groups of 0
    elements["group"] = elements["group"].replace(0, pd.NA)

    # Replace Nan groups with increasing numbers from 1 to total number of groups (with groupby)
    elements["group"] = elements["group"].fillna(
        elements.groupby("period")["group"].transform(
            lambda x: pd.RangeIndex(4, len(x) + 4)
        )
    )

    return elements


def pivot(elements):
    """Pivot the periodic table of elements.

    Must contain a cell entry to work.

    Arguments:
    ----------
    elements : pd.DataFrame
        The periodic table of elements.

    Returns:
    --------
    elements : pd.DataFrame
        The pivoted periodic table of elements.
    """
    # Check if the cell entry exists
    if "cell" not in elements.columns:
        raise ValueError("The DataFrame must contain a cell entry.")

    # Create the pivot table
    elements = elements.loc[:, ["cell", "period", "group"]]
    elements = elements.pivot(index="period", columns="group", values="cell")

    return elements
