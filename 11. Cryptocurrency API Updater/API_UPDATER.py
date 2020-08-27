import os
import pandas as pd
import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import xlwings as xw


def fetching_data():
    df = pd.read_excel("CryptoPortfolio.xlsx", index_col=None, header=0)
    coins = df["Name"]
    coins = [str(x).lower() for x in coins if str(x) != "nan"]
    coins_string = ",".join(coins)
    coins_string = str(coins_string)
    return coins, coins_string


def update_API(coins_string):
    url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'
    parameters = {
        'slug': coins_string
    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': '8f92b739-35b5-4617-8c0b-f0db4398ed0a',
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        print(data)
        coins_id = []
        names = []
        prices = []
        changes_1h = []
        changes_24h = []
        changes_7d = []
        for coin in data["data"]:
            coins_id.append(coin)

        for coin in coins_id:
            name = data["data"][coin]["name"]
            price = data["data"][coin]["quote"]["USD"]["price"]
            price = round(price, 5)
            change_1h = data["data"][coin]["quote"]["USD"]["percent_change_1h"]
            change_1h = round(change_1h, 2)
            change_24h = data["data"][coin]["quote"]["USD"]["percent_change_24h"]
            change_24h = round(change_24h, 2)
            change_7d = data["data"][coin]["quote"]["USD"]["percent_change_7d"]
            change_7d = round(change_7d, 2)
            names.append(name.lower())
            prices.append(price)
            changes_1h.append(change_1h)
            changes_24h.append(change_24h)
            changes_7d.append(change_7d)
        return names, prices, changes_1h, changes_24h, changes_7d

    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def sort_values(names, coins, prices, changes_1h, changes_24h, changes_7d):
    positions = []
    for i, coin in enumerate(coins):
        position = coins.index(names[i])
        positions.append(position)
    coins = [x for _, x in sorted(zip(positions, coins))]
    prices = [x for _, x in sorted(zip(positions, prices))]
    changes_1h = [x for _, x in sorted(zip(positions, changes_1h))]
    changes_24h = [x for _, x in sorted(zip(positions, changes_24h))]
    changes_7d = [x for _, x in sorted(zip(positions, changes_7d))]
    return prices, changes_1h, changes_24h, changes_7d


def update_to_xlsx(prices, changes_1h, changes_24h, changes_7d):
    wb = xw.Book('CryptoPortfolio.xlsx')
    sht1 = wb.sheets['PORTFOLIO']
    sht1.range('D2').options(transpose=True).value = prices
    sht1.range('F2').options(transpose=True).value = changes_1h
    sht1.range('G2').options(transpose=True).value = changes_24h
    sht1.range('H2').options(transpose=True).value = changes_7d
    wb.save()


def update():
    print("File found in given location. Proceeding to update values")
    coins, coins_string = fetching_data()
    names, prices, changes_1h, changes_24h, changes_7d = update_API(coins_string)
    print(f"Names: {names}")
    print(f"Prices: {prices}")
    print(f"1 Hour Changes: {changes_1h}")
    print(f"24 Hour Changes: {changes_24h}")
    print(f"7 Day Changes: {changes_7d}")
    if names == coins:
        print("Names=Coins")
        update_to_xlsx(prices, changes_1h, changes_24h, changes_7d)
    else:
        print("Sorting...")
        prices, changes_1h, changes_24h, changes_7d = sort_values(names, coins, prices, changes_1h, changes_24h,
                                                                  changes_7d)
        update_to_xlsx(prices, changes_1h, changes_24h, changes_7d)


if os.path.isfile("CryptoPortfolio.xlsx"):
    update()
else:
    print("File CryptoPortfolio.xlsx wasn't found.")
