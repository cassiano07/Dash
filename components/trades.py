import requests
from datetime import datetime
import pandas as pd


class Trades:

    def __init__(self, currency):
        url_trade = "https://www.mercadobitcoin.net/api/{}/trades/".format(currency)
        response = requests.get(url_trade)
        self.data = response.json()
        self.currency = currency

    def data_per_hour(self):
        items = []

        for row in self.data:
            date = datetime.strptime(datetime.utcfromtimestamp(int(row['date'])).strftime('%Y-%m-%d %H:%M:%S'),
                                     '%Y-%m-%d %H:%M:%S')

            summary_trades = {'date': date.strftime('%Y-%m-%d %H'),
                              'hour': date.hour,
                              'amount': row['amount'],
                              'price': row['price'],
                              'type': row['type']}

            items.append(summary_trades)

        df = pd.DataFrame(items)
        consolidated_data = df.groupby(['date', 'hour', 'type'], as_index=False).sum()
        return consolidated_data.to_json(orient='records')

    def quantity_of_trades(self):
        buy = []
        sell = []
        dates = []

        for row in self.data:
            if row["type"].lower() == 'sell':
                sell.append(row["tid"])
            elif row["type"].lower() == 'buy':
                buy.append(row["tid"])

            dates.append(datetime.utcfromtimestamp(int(row['date'])).strftime('%Y-%m-%d %H:%M:%S'))

        dates = sorted(dates)
        start_date = datetime.strptime(dates[0], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(dates.pop(), '%Y-%m-%d %H:%M:%S')

        consolidated_data = {"currency": self.currency,
                             "qty_buy": len(set(buy)),
                             "qty_sell": len(set(sell)),
                             "start_date": start_date,
                             "end_date": end_date}

        return consolidated_data

    def amount_negotiated(self):
        buy = 0
        sell = 0
        dates = []

        for row in self.data:
            if row["type"].lower() == 'sell':
                sell = sell + float(row['amount'])
            elif row["type"].lower() == 'buy':
                buy = buy + float(row['amount'])

            dates.append(datetime.utcfromtimestamp(int(row['date'])).strftime('%Y-%m-%d %H:%M:%S'))

        dates = sorted(dates)
        start_date = datetime.strptime(dates[0], '%Y-%m-%d %H:%M:%S')
        end_date = datetime.strptime(dates.pop(), '%Y-%m-%d %H:%M:%S')

        consolidated_data = {"currency": self.currency,
                             "amount_buy": "{:.8f}".format(buy),
                             "amount_sell": "{:.8f}".format(sell),
                             "start_date": start_date,
                             "end_date": end_date}

        return consolidated_data

