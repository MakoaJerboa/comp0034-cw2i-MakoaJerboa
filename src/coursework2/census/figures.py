from pathlib import Path
import pandas as pd
import plotly.express as px

yr2011file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2011.csv")
yr2021file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2021.csv")

def get_bar_2011(selected_hours):
    cols = ["Area", "All usual residents aged 16-74 in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2011 = pd.read_csv(yr2011file, usecols=cols)
    bar2011 = px.bar(data2011, x="Area", y=selected_hours, title="Census 2011", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2011

def get_bar_2021(selected_hours):
    cols = ["Area", "All usual residents aged 16+  in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2021 = pd.read_csv(yr2021file, usecols=cols)
    bar2021 = px.bar(data2021, x="Area", y=selected_hours, title="Census 2021", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2021

def get_pie_2011(selected_area):
    cols = ["Area", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2011 = pd.read_csv(yr2011file, usecols=cols)
    row = data2011[data2011["Area"] == selected_area]
    row.pop("Area")
    values = row.values.tolist()[0]
    pie2011 = px.pie(row, values=values, names=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title=f"Census 2011 worked hours for {selected_area}")
    return pie2011

def get_pie_2021(selected_area):
    cols = ["Area", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    data2021 = pd.read_csv(yr2021file, usecols=cols)
    row = data2021[data2021["Area"] == selected_area]
    row.pop("Area")
    values = row.values.tolist()[0]
    pie2011 = px.pie(row, values=values, names=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title=f"Census 2021 worked hours for {selected_area}")
    return pie2011