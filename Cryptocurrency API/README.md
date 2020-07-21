# The program allows you to create your own crypto portfolio in excel with up-to-date prices, percentage changes and a pie chart.

Requirements: Python 3, requests module, requests.exceptions, json, xlsxwriter

# Program:
1. asks the user to enter full names of the cryptocurrencies, e.g. bitcoin, xrp, cardano. After each single cryptocurrency entered, please hit enter.
2. by typing end, we stop the loop
3. if something goes wrong, the program will notify us about it
4. if everything is fine, the program asks us to enter a specific amount of each
 cryptocurrency as an integer (e.g. 5) or a decimal number (e.g. 0.4)
5. creates a CryptoPortfolio.xlsx file based on the entered data
6. saves the file in the program path
7. our excel has 6 columns "Name", "Short Name", "Quantity", "Price ($)", "Value ($)", "1H Change", "24H Change", "7D Change"
8. it also counts the total value of the wallet based on given amounts of cryptocurrencies
9. creates a pie chart showing the amounts of your cryptocurrencies

## The data is pulled from coinmarketcap.com using my private api key

