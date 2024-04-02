# Imports necessary modules
from dash import Dash, html, dcc
import dash_bootstrap_components as dbc

# Imports the chart functions from figures.py
from census.figures import get_bar_2011, get_bar_2021, get_pie_2011, get_pie_2021

# Defines charts with their initial values
bar_2011 = get_bar_2011("15 hours or less")
bar_2021 = get_bar_2021("15 hours or less")
pie_2011 = get_pie_2011("Barnet")
pie_2021 = get_pie_2021("Barnet")

# Defines the layout elements for each row of the dashboard:
    # The first row contains the title of the dashboard and a brief description
    # The second row contains the bar charts for 2011 and 2021
    # The third row contains the dropdowns for filtering the bar charts
    # The fourth row contains a brief description of the pie charts
    # The fifth row contains the pie charts for 2011 and 2021
    # The sixth row contains the dropdowns for filtering the pie charts

row_one = dbc.Row([
    dbc.Col([html.H1("2011 and 2021 Census Data Analytics"),
html.P(
    "You can filter which hours worker hour bands to show on the graphs using the dropdowns and can filter by area using click and drag on the graphs.")]),
])

row_two = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="bar_2011", figure=bar_2011)], width=6),
    dbc.Col(children=[dcc.Graph(id="bar_2021", figure=bar_2021)], width=6),
])

row_three = dbc.Row([
    dbc.Col(children=[dcc.Dropdown(id="dropdown-bar-2011",
                                     # id uniquely identifies the element, will be needed later
                                     options=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"],
                                     searchable=False, multi=True,
                                     value="15 hours or less"  # The default selection
                                     ),
                          ], width=2),
    dbc.Col(children=[], width={"size": 2, "offset": 2}),  # 4 'empty' columns between this and the previous column
    dbc.Col(children=[dcc.Dropdown(id="dropdown-bar-2021",
                                     # id uniquely identifies the element, will be needed later
                                     options=["15 hours or less", "16 to 30 hours", "31 to 48 hours", "49 or more hours"],
                                     searchable=False, multi=True,
                                     value="15 hours or less"  # The default selection
                                     ),
                          ], width=2),
    dbc.Col(children=[], width={"size": 2, "offset": 0}),  # 4 'empty' columns between this and the previous column
])

row_four = dbc.Row([
    dbc.Col([html.P("Pie charts for hours worked in 2011 and 2021. You can use the dropdowns to filter the hours worker hour bands by area. The dropdowns also work as search boxes."),]),
])

row_five = dbc.Row([
    dbc.Col(children=[dcc.Graph(id="pie_2011", figure=pie_2011)], width=6),
    dbc.Col(children=[dcc.Graph(id="pie_2021", figure=pie_2021)], width=6),
])

row_six = dbc.Row([
    dbc.Col(children=[dcc.Dropdown(id="dropdown-pie-2011",
                                     # id uniquely identifies the element, will be needed later
                                     options=["Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden", "City of London", "Croydon", "Ealing", 
                                              "Enfield", "Greenwich", "Hackney", "Hammersmith and Fulham", "Haringey", "Harrow", "Havering", "Hillingdon", "Hounslow", "Islington", 
                                              "Kensington and Chelsea", "Kingston upon Thames", "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge", "Richmond upon Thames", 
                                              "Southwark", "Sutton", "Tower Hamlets", "Waltham Forest", "Wandsworth", "Westminster"],
                                     searchable=True, multi=False,
                                     value="Barnet"  # The default selection
                                     ),], width=6),
    dbc.Col(children=[dcc.Dropdown(id="dropdown-pie-2021",
                                     # id uniquely identifies the element, will be needed later
                                     options=["Barking and Dagenham", "Barnet", "Bexley", "Brent", "Bromley", "Camden", "City of London", "Croydon", "Ealing", 
                                              "Enfield", "Greenwich", "Hackney", "Hammersmith and Fulham", "Haringey", "Harrow", "Havering", "Hillingdon", "Hounslow", "Islington", 
                                              "Kensington and Chelsea", "Kingston upon Thames", "Lambeth", "Lewisham", "Merton", "Newham", "Redbridge", "Richmond upon Thames", 
                                              "Southwark", "Sutton", "Tower Hamlets", "Waltham Forest", "Wandsworth", "Westminster"],
                                     searchable=True, multi=False,
                                     value="Barnet"  # The default selection
                                     ),], width=6),
    ])