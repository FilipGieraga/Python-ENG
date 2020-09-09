import json
from requests import Request, Session
from requests.exceptions import ConnectionError, Timeout, TooManyRedirects
import xlsxwriter
from configparser import ConfigParser

file = 'config.ini'
config= ConfigParser()
config.read(file)


def input_data():
    print("Disclaimer 1: Please provide coin full name e.g. Bitcoin instead of BTC.")
    print('Disclaimer 2: To stop the loop enter "end" as coin name.')
    print('Disclaimer 3: If coin has a space you have to use -. Example : Binance Coin = binance-coin')
    coin_names = []
    coin_name = ''
    while coin_name != "end":
        coin_name = str(input("Please provide a coin name:\n"))
        if coin_name == "end":
            coin_names = ",".join(coin_names)
            return coin_names
        coin_name = coin_name.lower()
        coin_names.append(coin_name)
        print(coin_names)


def API_information(coins):
    url = config['path']['url']
    parameters = {
        'slug': coins

    }
    headers = {
        'Accepts': 'application/json',
        'X-CMC_PRO_API_KEY': config['path']['api_key'],
    }

    session = Session()
    session.headers.update(headers)

    try:
        response = session.get(url, params=parameters)
        data = json.loads(response.text)
        coins_id = []
        coin_full_names = []
        coin_short_names = []
        prices = []
        changes_1h = []
        changes_24h = []
        changes_7d = []
        for coin in data["data"]:
            coins_id.append(coin)

        for coin in coins_id:
            name = data["data"][coin]["name"]
            name = name.title()
            symbol = data["data"][coin]["symbol"]
            symbol = symbol.upper()
            price = data["data"][coin]["quote"]["USD"]["price"]
            price = round(price, 5)
            change_1h = data["data"][coin]["quote"]["USD"]["percent_change_1h"]
            change_1h = round(change_1h, 2)
            change_24h = data["data"][coin]["quote"]["USD"]["percent_change_24h"]
            change_24h = round(change_24h, 2)
            change_7d = data["data"][coin]["quote"]["USD"]["percent_change_7d"]
            change_7d = round(change_7d, 2)
            coin_full_names.append(name)
            coin_short_names.append(symbol)
            prices.append(price)
            changes_1h.append(change_1h)
            changes_24h.append(change_24h)
            changes_7d.append(change_7d)
        return coin_full_names, coin_short_names, prices, changes_1h, changes_24h, changes_7d


    except (ConnectionError, Timeout, TooManyRedirects) as e:
        print(e)


def quan(coin_full_names):
    quantities = []
    i = 0
    while i < len(coin_full_names):
        while True:
            try:
                quantity = float(input(f"Enter the amount of coin {coin_full_names[i]}:\n"))
                i += 1
            except:
                print("Wrong value, please try again.")
            else:
                quantities.append(quantity)
                break
    return quantities


def excel_file(quantities, coin_full_names, coin_short_names, prices, changes_1h, changes_24h, changes_7d):
    workbook = xlsxwriter.Workbook(str(config['name']['file']))
    worksheet = workbook.add_worksheet(name="PORTFOLIO")

    main_headlines = ["Name", "Short Name", "Quantity", "Price($)", "Value($)", "1H Change", "24H Change", "7D Change"]
    cell_format = workbook.add_format({'bold': True})

    row = 0
    col = 0

    for head in (main_headlines):
        worksheet.write(row, col, head, cell_format)
        col += 1

    row = 1
    col = 0

    for full_name in coin_full_names:
        worksheet.write(row, col, full_name)
        row += 1

    row = 1
    col = 1

    for short_name in coin_short_names:
        worksheet.write(row, col, short_name)
        row += 1

    row = 1
    col = 2

    for quantity in quantities:
        worksheet.write(row, col, quantity)
        row += 1

    row = 1
    col = 3

    for price in prices:
        worksheet.write(row, col, price)
        row += 1

    row = 1
    col = 4

    for i1 in range(len(coin_full_names)):
        worksheet.write(row, col, '=(C' + str(row + 1) + '*D' + str(row + 1) + ')')
        row += 1

    row = 1
    col = 5

    for change_1h in changes_1h:
        worksheet.write(row, col, change_1h)
        row += 1

    row = 1
    col = 6

    for change_24h in changes_24h:
        worksheet.write(row, col, change_24h)
        row += 1

    row = 1
    col = 7

    for change_7d in changes_7d:
        worksheet.write(row, col, change_7d)
        row += 1

    worksheet.conditional_format('F2:H' + str(row) + '', {'type': '3_color_scale'})

    worksheet.write(row, 5, 'Total', cell_format)
    worksheet.write(row, 4, '=SUM(E1:E' + str(row) + ')')

    chart1 = workbook.add_chart({'type': 'pie'})

    chart1.add_series({
        'name': 'Values of coins',
        'categories': ['PORTFOLIO', 1, 1, len(coin_short_names), 1],
        'values': ['PORTFOLIO', 1, 4, len(coin_short_names), 4],
    })

    chart1.set_title({'name': 'Values of coins'})

    chart1.set_style(10)

    worksheet.insert_chart('J' + str(row + 2) + '', chart1, {'x_offset': 25, 'y_offset': 10})


    workbook.close()


while True:
    try:
        coins = input_data()
        coin_full_names, coin_short_names, prices, changes_1h, changes_24h, changes_7d = API_information(coins)
        quantities = quan(coin_full_names)
        excel_file(quantities, coin_full_names, coin_short_names, prices, changes_1h, changes_24h, changes_7d)
    except Exception as error:
        print(f"Something went wrong: {error}. Try again...")
    else:
        break
