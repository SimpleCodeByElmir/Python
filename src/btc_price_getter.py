# This program gets price of BTCUSTD from Binance every n seconds

import requests
import time

url = "https://api.binance.com/api/v3/ticker/price"

btc_prices = []

for i in range(10):
    response = requests.get(url, params={"symbol": 'BTCUSDT'})
    price = float(response.json()['price'])
    btc_prices.append(price)
    time.sleep(2)  # n = 2 (sleep for 2 seconds)

print(btc_prices)
