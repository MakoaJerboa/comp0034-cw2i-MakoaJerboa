# Imports necessary modules
from dash import Dash, html, Input, Output
import dash_bootstrap_components as dbc

# Imports the layout elements from layout_elements.py
from census.layout_elements import get_bar_2011, get_bar_2021, get_pie_2011, get_pie_2021
from census.layout_elements import row_one, row_two, row_three, row_four, row_five, row_six

# Variable that contains the external_stylesheet to use, in this case Bootstrap styling from dash bootstrap components (dbc)
external_stylesheets = [dbc.themes.BOOTSTRAP]

# Define a variable that contains the meta tags
meta_tags = [
    {"name": "viewport", "content": "width=device-width, initial-scale=1"},
]

# Pass the stylesheet and meta_tag variables to the Dash app constructor
app = Dash(__name__, external_stylesheets=external_stylesheets, meta_tags=meta_tags)

# Defines the layout of the dashboard, using the rows defined in layout_elements.py
app.layout = dbc.Container(
    html.Div([
    row_one,
    row_two,
    row_three,
    row_four,
    row_five,
    row_six,
])
)

# Callbacks to update the charts based on the dropdown selections:
    # The first callback updates the 2011 bar chart based on the selected worked hours band
    # The second callback updates the 2021 bar chart based on the selected worked hours band
    # The third callback updates the 2011 pie chart based on the selected area
    # The fourth callback updates the 2021 pie chart based on the selected area
@app.callback(
    [Output("bar_2011", "figure")],
    [Input("dropdown-bar-2011", "value")],
)
def update_bar_2011(selected_hours):
    bar_2011 = get_bar_2011(selected_hours)
    return [bar_2011]

@app.callback(
    [Output("bar_2021", "figure")],
    [Input("dropdown-bar-2021", "value")],
)
def update_bar_2021(selected_hours):
    bar_2021 = get_bar_2021(selected_hours)
    return [bar_2021]

@app.callback(
    [Output("pie_2011", "figure")],
    [Input("dropdown-pie-2011", "value")],
)
def update_pie_2011(selected_area):
    pie_2011 = get_pie_2011(selected_area)
    return [pie_2011]

@app.callback(
    [Output("pie_2021", "figure")],
    [Input("dropdown-pie-2021", "value")],
)
def update_pie_2021(selected_area):
    pie_2021 = get_pie_2021(selected_area)
    return [pie_2021]

# Runs the app
if __name__ == '__main__':
    app.run(debug=True)