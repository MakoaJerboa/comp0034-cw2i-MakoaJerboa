# Imports necessary modules
from pathlib import Path
import pandas as pd
import plotly.express as px

# Sets the paths for each data file
yr2011file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2011.csv")
yr2021file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2021.csv")


def get_bar_2011(selected_hours):
    """
    Generates a bar chart for the number of workers in each worked hours band sorted by area in 2011.

    Attributes:
    selected_hours (list of strings): The selected worked hours band, multiple can be selected.
    cols (list of strings): The columns to be used from the dataset.
    data2011 (pandas.DataFrame): The dataframe for the year 2011.

    Returns:
    bar2011 (plotly.graph_objects.Figure): The generated bar chart for the number of workers in the year 2011.
    """
    cols = ["Area", "All usual residents aged 16-74 in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2011 = pd.read_csv(yr2011file, usecols=cols)
    bar2011 = px.bar(data2011, x="Area", y=selected_hours, title="Census 2011", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2011

def get_bar_2021(selected_hours):
    """
    Generates a bar chart for the number of workers in each worked hours band sorted by area in 2021.

    Attributes:
    selected_hours (list of strings): The selected worked hours band, multiple can be selected.
    cols (list of strings): The columns to be used from the dataset.
    data2021 (pandas.DataFrame): The dataframe for the year 2021.

    Returns:
    bar2021 (plotly.graph_objects.Figure): The generated bar chart for the number of workers in the year 2021.
    """
    cols = ["Area", "All usual residents aged 16+  in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2021 = pd.read_csv(yr2021file, usecols=cols)
    bar2021 = px.bar(data2021, x="Area", y=selected_hours, title="Census 2021", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2021

def get_pie_2011(selected_area):
    """
    Generates a pie chart for the number of workers in each worked hours band based on the selected area in the year 2011.

    Attributes:
    selected_area (string): The selected area to generate the pie chart for.
    cols (list of strings): The columns to be used from the dataset.
    data2011 (pandas.DataFrame): The dataframe for the year 2011.
    row (pandas.DataFrame): The row of the selected area.
    values (list of int): The values of the selected area.

    Returns:
    pie2011 (plotly.graph_objects.Figure): The generated pie chart for the number of workers in each worked hours band for the selected area for the year 2011.
    """
    cols = ["Area", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2011 = pd.read_csv(yr2011file, usecols=cols)
    row = data2011[data2011["Area"] == selected_area]
    row.pop("Area")
    values = row.values.tolist()[0]
    pie2011 = px.pie(row, values=values, names=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title=f"Census 2011 worked hours for {selected_area}")
    return pie2011

def get_pie_2021(selected_area):
    """
    Generates a pie chart for the number of workers in each worked hours band based on the selected area in the year 2021.

    Attributes:
    selected_area (string): The selected area to generate the pie chart for.
    cols (list of strings): The columns to be used from the dataset.
    data2021 (pandas.DataFrame): The dataframe for the year 2021.
    row (pandas.DataFrame): The row of the selected area.
    values (list of int): The values of the selected area.

    Returns:
    pie2011 (plotly.graph_objects.Figure): The generated pie chart for the number of workers in each worked hours band for the selected area for the year 2021.
    """
    cols = ["Area", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2021 = pd.read_csv(yr2021file, usecols=cols)
    row = data2021[data2021["Area"] == selected_area]
    row.pop("Area")
    values = row.values.tolist()[0]
    pie2011 = px.pie(row, values=values, names=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title=f"Census 2021 worked hours for {selected_area}")
    return pie2011