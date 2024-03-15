from pathlib import Path
import pandas as pd
import plotly.express as px

def get_bar_2011():
    cols = ["Area", "All usual residents aged 16-74 in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    yr2011file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2011.csv")
    data2011 = pd.read_csv(yr2011file, usecols=cols)
    bar2011 = px.bar(data2011, x="Area", y=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title="Census 2011", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2011

def get_bar_2021():
    cols = ["Area", "All usual residents aged 16+  in employment", "15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"]
    yr2021file = Path(__file__).parent.parent.joinpath("data", "dataset_prepared_2021.csv")
    data2021 = pd.read_csv(yr2021file, usecols=cols)
    bar2021 = px.bar(data2021, x="Area", y=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"], title="Census 2021", labels={"value": "Number of workers", "variable": "Number of hours worked"})
    return bar2021