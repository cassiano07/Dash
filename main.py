from dash import Dash
from dash.html import Div
import dash_bootstrap_components as bc
from dash import Input, Output, State, html

# components criados
from components import graph, navbar

# Components

# cards
row_cards = graph.row_cards()

navbar = navbar.navbar()

# graph trades
trade_per_date = graph.trade_per_date()
trade_per_hour = graph.trade_per_hour()


body = Div(
    children=[
        navbar,
        row_cards,

        # add graphs
        bc.Row(
            [
                bc.Col(trade_per_date, width="auto"),
                bc.Col(trade_per_hour, width="auto"),
            ],
            className="d-flex justify-content-center align-items-center m-3",
            align="center",
            justify="center"
        )

    ]
)

app = Dash(__name__, external_stylesheets=[bc.themes.DARKLY, bc.icons.FONT_AWESOME],  meta_tags=[
        {"name": "viewport", "content": "width=device-width, initial-scale=1"}
    ])

app.layout = body

# add callback for toggling the collapse on small screens
@app.callback(
    Output("navbar-collapse", "is_open"),
    [Input("submit-button", "n_clicks")],
    [State("select", "value")],
)
def toggle_navbar_collapse(n, is_open):
    if n:
        print(is_open, 'true')
    print(is_open, 'false')

app.run_server(debug=True)



