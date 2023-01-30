"""
Crypto prices
"""

from requests import Request, Session
import json
from bs4 import BeautifulSoup  # web scraping
import pandas as pd
import pprint

url = "https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest"


coins_of_interest = "ETH,MATIC,SOL,AVAX,CRV"

parameters = {"symbol": coins_of_interest, "convert": "USD"}

headers = {
    "Accepts": "application/json",
    "X-CMC_PRO_API_KEY": "01ae1c8b-2b5e-4d7c-8baa-dd58380bc39d",
}

session = Session()
session.headers.update(headers)

response = session.get(url, params=parameters)
response_data = json.loads(response.text)


# pprint.pprint(response_data)

coin_data = {}

selected_keys = [
    "percent_change_1h",
    "percent_change_24h",
    "percent_change_30d",
    "percent_change_60d",
    "percent_change_7d",
    "percent_change_90d",
    "price",
]

for coin in coins_of_interest.split(","):
    coin_data[coin] = response_data["data"][coin]["quote"]["USD"]

    for key in list(coin_data[coin].keys()):
        if key not in selected_keys:

            coin_data[coin].pop(key)
        elif key == "price":
            coin_data[coin][key] = round(coin_data[coin][key], 3)
        else:
            coin_data[coin][key.split("_")[-1]] = round(coin_data[coin][key], 1)
            coin_data[coin].pop(key)

# pprint.pprint(coin_data)

coin_df = pd.DataFrame.from_dict(coin_data, orient="index")

pd.set_option("display.width", 200)
pd.set_option("display.max_columns", 8)


def color(val):
    if val > 2:
        color = "green"
    elif val < -2:
        color = "red"
    else:
        color = "yellow"

    return "background-color: %s" % color


coin_df.style.applymap(color, subset=["24h"])

print(coin_df)

coin_df.to_csv("./crypt_data.csv")
