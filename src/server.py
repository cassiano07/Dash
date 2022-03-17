import dash_bootstrap_components as bc
from dash import Dash

app = Dash('Dash', external_stylesheets=[bc.themes.DARKLY, bc.icons.FONT_AWESOME], meta_tags=[
    {"name": "viewport", 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}
])
