import requests
import pandas as pd
import json


class Trades:
    """
    Consult the Mercado Bitcoin API to extract data.
    Performs the manipulation and treatment of data to be presented in graphs.
    """

    def __init__(self, currency):
        self.currency = currency
        url_trade = "https://www.mercadobitcoin.net/api/{}/trades/".format(currency)
        response = requests.get(url_trade)
        self.data = response.json()

        if response.status_code == 200:
            self.df = pd.DataFrame(response.json())
            self.df['date'] = pd.to_datetime(self.df['date'], unit='s')
        else:
            self.df = None

    def data_per_hour(self):
        """
        This function groups the data by hour.
        :return: return a Dataframe.
        """

        df_hour = self.df.copy()

        # remove columns
        del df_hour['price'], df_hour['tid']

        # change date format
        df_hour['date'] = pd.to_datetime(df_hour['date'].dt.strftime('%Y-%m-%d %H'))

        # aggregated data
        aggregated_data = df_hour.groupby(['date', 'type'], as_index=False).sum()

        return aggregated_data

    def data_per_date(self):
        """
        A copy of the main dataframe is made and some columns are removed from the dataframe.
        :return: return a Dataframe.
        """

        df_date = self.df.copy()

        # remove columns
        del df_date['price'], df_date['tid']

        return df_date

    def quantity_of_trades(self):
        """
        Counts purchases and sales made.
        :return: a json with the summarized data.
        """

        df_quantity = self.df.copy()

        # remove columns
        del df_quantity['price'], df_quantity['tid'], df_quantity['amount'], df_quantity['date']

        # count data and convert in dict
        aggregated_data = json.loads(df_quantity['type'].value_counts().to_json())

        return aggregated_data

    def total_negotiated(self):
        """
        Generate the total amount traded.
        :return: A Dataframe.
        """
        df_total = self.df.copy()

        del df_total['date'], df_total['tid'], df_total['price']

        aggregated_data = df_total.groupby('type', as_index=False).sum()

        return aggregated_data
