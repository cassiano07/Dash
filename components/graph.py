import dash_bootstrap_components as bc
from dash import html
from dash.dcc import Graph
from components.trades import Trades
import plotly.express as px
import pandas

trade = Trades('BTC')


def trade_per_date():
    data_per_date = trade.data_per_date( )

    fig = px.line(
        data_per_date,
        x="date",
        y="amount",
        color='type',
        title='Trades',
        color_discrete_map={"buy": "#de4f3a", "sell": "#722731"}
    )

    fig.update_layout(
        {
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'xaxis': {
                'showgrid': False
            },
            'yaxis': {
                'showgrid': False
            },
            'font': {
                'color': '#e4b302'
            },
            'title_x': 0.5
        },
        yaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_title=''
    )

    graph = Graph(figure=fig)

    card = bc.Card(
        bc.CardBody(
            graph,
        ),
    )

    return card


def trade_per_hour():
    # graph per hour
    data_per_hour = trade.data_per_hour( )

    fig_per_hour = px.bar(data_per_hour, x="date", y="amount", color='type', title='Hourly Trades',
                          color_discrete_map={
                              "buy": "#158fa2",
                              "sell": "#e4b302"
                          },
                          text_auto=True
                          )

    fig_per_hour.update_layout(
        {
            'plot_bgcolor': 'rgba(0, 0, 0, 0)',
            'paper_bgcolor': 'rgba(0, 0, 0, 0)',
            'xaxis': {
                'showgrid': False
            },
            'yaxis': {
                'showgrid': False
            },
            'font': {
                'color': '#e4b302'
            },
            'title_x': 0.5
        },

        # Remove axis y
        yaxis_visible=False,
        yaxis_showticklabels=False,
        xaxis_title=''
    )

    graph = Graph(figure=fig_per_hour)

    card = bc.Card(
        bc.CardBody(
            graph,
        ),
    )

    return card


def make_tooltip(target, message):
    return bc.Tooltip(
        message,
        target=target,
    )


# Primeiro defino uma função para criar os cards
def kpi(data, type=None, model=None, id=None, message_tooltip=None):
    if model == 'buy':
        color = '#2CA02C'
        icon = 'fas fa-caret-up me-2 fa-2x'
    else:
        color = '#D62728'
        icon = 'fas fa-caret-down me-2 fa-2x'

    if type == 'quantity':

        info = [
            bc.Row(
                [
                    bc.Col(html.I(className=icon, style={'color': color}), width="auto"),
                    bc.Col(html.H3(data, className="card-title"), width="auto"),
                ],
                className="d-flex justify-content-center align-items-center",
            )
        ]

    else:
        info = [
            bc.Row(
                [
                    bc.Col(html.H3(data, className="card-title", style={'color': color}), width="auto")
                ],
                className="d-flex justify-content-center align-items-center",
            )
        ]

    card = bc.Card(
        bc.CardBody(
            info,
        ),
        id=id,
        style={"width": "18rem"},
    )

    tooltip = make_tooltip(id, message_tooltip)

    return card, tooltip


# aqui crio uma linha e adiciono os cards criados centralizando os mesmos
def row_cards():
    data = trade.amount_negotiated( )

    quantity_of_trades = trade.quantity_of_trades( )

    card_quantity_buy = kpi(quantity_of_trades['qty_buy'], 'quantity', 'buy', id='card_quantity_buy',
                            message_tooltip='Quantity buy')
    card_amount_buy = kpi(data['amount_buy'], model='buy', id='card_amount_buy',
                          message_tooltip='Amount buy')
    card_amount_sell = kpi(data['amount_sell'], model='sell', id='card_amount_sell',
                           message_tooltip='Amount sell')
    card_quantity_sell = kpi(quantity_of_trades['qty_sell'], 'quantity', 'sell',
                             id='card_quantity_sell', message_tooltip='Quantity sell')

    cards = bc.Row(
        [
            bc.Col(card_quantity_buy, width="auto"),
            bc.Col(card_amount_buy, width="auto"),
            bc.Col(card_amount_sell, width="auto"),
            bc.Col(card_quantity_sell, width="auto")
        ],
        className="d-flex justify-content-center align-items-center m-3",
        align="center",
        justify="center"
    )

    return cards
