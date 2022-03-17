import dash_bootstrap_components as bc
from dash import html
from dash.dcc import Graph
from src.data.trades import Trades
import plotly.express as px

trade = Trades('BTC')


class Graphics:
    """
    Creates all the graphs that will show on the dashboard
    """

    def __init__(self, cryptocurrency):
        trades = Trades(cryptocurrency)
        self.df_total = trades.total_negotiated()
        self.json_quantity = trades.quantity_of_trades()
        self.df_per_hour = trades.data_per_hour()
        self.detailed_df = trades.data_per_date()

    @staticmethod
    def __cards(component, graph=None, card_id=None):
        """
        Inserts received components into a bootstrap card

        :param component: Dash or bootstrap components
        :param graph: tells if the component is a graphic
        :param card_id: An id that will be used to place a card identifier
        :return: a bootstrap component card
        """

        if graph:
            body = Graph(figure=component)

        else:
            body = component

        card = bc.Card(
            bc.CardBody(
                body,
            ),
            className="m-2",
            id=card_id
        )

        return card

    @staticmethod
    def __make_tooltip(target, message):
        """
        Create tooltip for a component
        :param target: component id
        :param message: message to be added in tooltip
        :return: bootstrap tooltip component
        """
        return bc.Tooltip(
            message,
            target=target,
        )

    def __create_kpi(self, data, card_id=None, title=None):
        """
        Create dashboard kpis
        :param data: the kpi data
        :param card_id: unique id for component
        :param title: kpi title
        :return: kpi cards
        """

        body = [
            bc.Row(
                [
                    bc.Col(html.H5(title, style={'color': '#e4b302'}), width="auto"),
                    bc.Col(html.H5(data, className="card-title", style={'color': '#8fc9b9'}), width="auto"),
                ],
                className="d-flex flex-column justify-content-center align-items-center",
            )
        ]

        card = self.__cards(component=body, card_id=card_id)

        return card

    def line_per_date(self):
        """
        Build the detailed line chart
        :return: card with graph and tooltip
        """
        fig = px.line(
            self.detailed_df,
            x="date",
            y="amount",
            color='type',
            title='Trades',
            line_shape='spline',
            color_discrete_map={"buy": "#8fc9b9", "sell": "#e4b302"}
        )

        fig.update_layout(
            {
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                'font': {
                    'color': '#e4b302'
                },
                'title_x': 0.5
            },
            yaxis_visible=False,
            xaxis_showgrid=False,
            yaxis_showticklabels=False,
            xaxis_title=''
        )

        tooltip = self.__make_tooltip(target='line_per_date', message='show the last 1.000 trades on the exact date')

        return self.__cards(component=fig, graph=True, card_id='line_per_date'), tooltip

    def doughnut(self):
        """
        Build the dashboard donut chart
        :return: card with graph and tooltip
        """
        fig = px.pie(
            self.df_total, values=self.df_total['amount'],
            names=self.df_total['type'],
            title='Buy and Sell Percentage',
            hole=.5,
            color=self.df_total['type'],
            color_discrete_map={"buy": "#02779e", "sell": "#63d3ff"}
        )

        fig.update_layout(
            {
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                'font': {
                    'color': '#e4b302'
                },
                'title_x': 0.5
            },
            yaxis_visible=False,
            xaxis_showgrid=False,
            yaxis_showticklabels=False,
            xaxis_title=''
        )

        tooltip = self.__make_tooltip(target='doughnut', message='show the total traded in percentage')

        return self.__cards(component=fig, graph=True, card_id='doughnut'), tooltip

    def line_per_hour(self):
        """
        Build the hourly line chart
        :return: card with graph and tooltip
        """
        fig = px.line(self.df_per_hour,
                      x="date",
                      line_shape='spline',
                      y="amount", color='type',
                      title='Hourly Trades',
                      color_discrete_map={"buy": "#158fa2", "sell": "#e4b302"},
                      markers=True
                      )

        fig.update_layout(
            {
                'plot_bgcolor': 'rgba(0, 0, 0, 0)',
                'paper_bgcolor': 'rgba(0, 0, 0, 0)',
                'font': {
                    'color': '#e4b302'
                },
                'title_x': 0.5
            },
            yaxis_visible=False,
            xaxis_showgrid=False,
            yaxis_showticklabels=False,
            xaxis_title=''
        )

        tooltip = self.__make_tooltip(target='line_per_hour', message='show the last 1.000 trades per hour')

        return self.__cards(component=fig, graph=True, card_id='line_per_hour'), tooltip

    def cards(self):
        """
        Makes a call to the KPI creation functions so that they are created.
        :return: cards kpis
        """
        if self.json_quantity.get('buy'):

            quantity_buy = self.__create_kpi(
                data=self.json_quantity['buy'],
                card_id='quantity_buy',
                title='Quantity buy',

            )

            amount_buy = self.__create_kpi(
                data=self.df_total.iloc[0]['amount'],
                card_id='amount_buy',
                title='Amount buy',
            )

        else:
            quantity_buy = None
            amount_buy = None

        if self.json_quantity.get('sell'):
            quantity_sell = self.__create_kpi(
                data=self.json_quantity['sell'],
                card_id='quantity_sell',
                title='Quantity sell',
            )

            amount_sell = self.__create_kpi(
                data=self.df_total.iloc[1]['amount'],
                card_id='amount_sell',
                title='Amount Sell',
            )
        else:
            amount_sell = None
            quantity_sell = None

        return quantity_buy, amount_buy, amount_sell, quantity_sell