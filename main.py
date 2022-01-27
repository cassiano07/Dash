from dash import Dash
from dash.html import Div
import dash_bootstrap_components as bc
from components import graph, navbar

# Components

graphics = graph.graphics()

navbar = navbar.navbar()

body = Div(
    children=[
        navbar,
        graphics
    ]
)

app = Dash(__name__, external_stylesheets=[bc.themes.DARKLY],  meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

app.layout = body

app.run_server(debug=True)