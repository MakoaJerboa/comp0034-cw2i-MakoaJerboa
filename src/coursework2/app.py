# Imports for Dash and Dash.html
from dash import Dash, html
import dash_bootstrap_components as dbc

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

app.layout = dbc.Container(
    html.Div([
    html.Div(children='My First App with Data, Graph, and Controls',
             style={'textAlign': centre, colour: 'blue', 'fontSize': 30}),
    html.Div(children='Hello World'),
])
)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)