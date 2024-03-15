# Imports for Dash and Dash.html
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from census.figures import get_bar_2011, get_bar_2021

# Defines charts
bar_2011 = get_bar_2011()
bar_2021 = get_bar_2021()

# Allows me to spell centre and colour correctly
centre="center"
colour = "color"

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.CYBORG]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)



row_one = dbc.Row([
    dbc.Col([html.H1("Census Data Analytics"),
html.P(
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Praesent congue luctus elit nec gravida. Fusce efficitur posuere metus posuere malesuada. ")]),
])

row_two = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="bar_2011", figure=bar_2011)], width=6),
    dbc.Col(children=[dcc.Graph(id="bar_2021", figure=bar_2021)], width=6),
])

row_three = dbc.Row([
    dbc.Col(children=[dbc.Select(id="dropdown-2011",
                                     # id uniquely identifies the element, will be needed later
                                     options=[
                                         {"label": "15 hours or less", "value": "15 hours or less"},
                                         # The value is in the format of the column heading in the data
                                         {"label": "16 to 30 hours", "value": "16 to 30 hours"},
                                         {"label": "31 to 48 hours", "value": "31 to 48 hours"},
                                         {"label": "49 or more hours", "value": "49 or more hours"},
                                     ],
                                     value="15 hours or less"  # The default selection
                                     ),
                          ], width=2),
    dbc.Col(children=[], width={"size": 2, "offset": 2}),  # 4 'empty' columns between this and the previous column
    dbc.Col(children=[dbc.Select(id="dropdown-2021",
                                     # id uniquely identifies the element, will be needed later
                                     options=[
                                         {"label": "15 hours or less", "value": "15 hours or less"},
                                         # The value is in the format of the column heading in the data
                                         {"label": "16 to 30 hours", "value": "16 to 30 hours"},
                                         {"label": "31 to 48 hours", "value": "31 to 48 hours"},
                                         {"label": "49 or more hours", "value": "49 or more hours"},
                                     ],
                                     value="15 hours or less"  # The default selection
                                     ),
                          ], width=2),
    dbc.Col(children=[], width={"size": 2, "offset": 0}),  # 4 'empty' columns between this and the previous column
])

row_four = dbc.Row([
    dbc.Col(children=[], width=6),
    dbc.Col(children=[], width=6),
])

app.layout = dbc.Container(
    html.Div([
    html.Div(children='My First App with Data, Graph, and Controls',
             style={'textAlign': centre, colour: 'blue', 'fontSize': 30}),
    html.Div(children='Hello World'),
    row_one,
    row_two,
    row_three,
    row_four,
])
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
