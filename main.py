from dash import Dash
import dash_bootstrap_components as bc
from dash import Input, Output, State, html
from components import graph, navbar

# menu
navbar = navbar.navbar()

# screen body
body = html.Div(
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

app = Dash(__name__, external_stylesheets=[bc.themes.DARKLY, bc.icons.FONT_AWESOME], meta_tags=[
    {"name": "viewport", 'content': 'width=device-width, initial-scale=1.0, maximum-scale=1.2, minimum-scale=0.5,'}
])

app.layout = body


@app.callback(
    [
        Output("navbar-collapse", "is_open"),
        Output("grapichs", "children"),
    ],
    [
        Input("submit-button", "n_clicks"),
    ],
    [State("select", "value")],
)
def toggle_navbar_collapse(action, currency):
    if action:
        grapichs = graph.Graphics(currency)
    else:
        grapichs = graph.Graphics(currency)

    doughnut = grapichs.doughnut()
    line_per_date = grapichs.line_per_date()
    line_per_hour = grapichs.line_per_hour()
    cards = grapichs.cards()

    cols = (
        bc.Col(cards[0], xs=12, sm=12, md=6, lg=3),
        bc.Col(cards[1], xs=12, sm=12, md=6, lg=3),
        bc.Col(cards[2], xs=12, sm=12, md=6, lg=3),
        bc.Col(cards[3], xs=12, sm=12, md=6, lg=3),
        bc.Col(line_per_date, width=12),
        bc.Col(line_per_hour, xs=12, sm=12, md=12, lg=6),
        bc.Col(doughnut, xs=12, sm=12, md=12, lg=6)
    )

    return currency, cols


app.run_server(debug=False, host="0.0.0.0")
