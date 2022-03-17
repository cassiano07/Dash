import dash_bootstrap_components as bc
from dash import Input, Output, State

from src.components import graph
from src.app import app


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
def waiting_for_user_action(action, currency):
    """
    Waits for user actions in the currency selection field to be able to update the charts
    :param action: report a user action
    :param currency: selected cryptocurrency
    :return: updated charts based on selected currency data
    """
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
