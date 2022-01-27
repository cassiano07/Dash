import requests
import json

url_trade = "https://www.mercadobitcoin.net/api/BTC/trades/"


response = requests.get(url_trade)

data = response.json()

buy = []
sell = []

for trade in data:
    if trade["type"].lower() == 'sell':
        sell.append(trade["tid"])
    else:
        sell.append(trade["tid"])
    print(trade["tid"])

# print(response.json())

