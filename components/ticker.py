import requests
from datetime import datetime
import pandas as pd


class Ticker:

    def __init__(self, currency):
        url_trade = "https://www.mercadobitcoin.net/api/{}/ticker/".format(currency)
        response = requests.get(url_trade)
        self.data = response.json()
        self.currency = currency

    def summary_24_hours(self):
        consolidated_data = self.data['ticker']

        return consolidated_data
