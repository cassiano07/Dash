import dash_bootstrap_components as bc
from dash import html

from .server import app
from src.components import navbar
from .callbacks import update_layout

# menu
navbar = navbar.navbar()

# screen body
app.layout = html.Div(
    children=[
        navbar,

        # graphics
        bc.Row(
            id="grapichs",
            style={'width': '100%'},
        )

    ],
    style={'width': '100%'},
    className="d-flex flex-column justify-content-center align-items-center",
)