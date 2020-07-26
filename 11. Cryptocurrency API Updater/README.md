# Cryptocurrency API extension allows you to update the prices in the CryptoPortfolio.xlsx file by running the script

Requirements: Python 3, os module, pandas module, json module, requests module, requests.exceptions module, xlwings module

# Program:
1. searches for CryptoPortfolio.xlsx file and checks if it exists in the path where the program is located
2. checks the Name column to find the coins we have in our wallet
3. update values ​​such as price and percentage changes
4. based on these changes, values ​​such as total, value(which is a current price of coin) and the appearance of the chart change


# Important:
The program allows us to make changes to the excel file and then run the script.
Let's assume that we want to add a new coin to our wallet and change the amount of the existing coin. <br>
To change the amount of a coin, just change the number in the corresponding cell of quantity. <br>
To add a new coin we need to extend the formulas in our file, we need to move cells of Total and the corresponding value down by one in this case.
This creates a new empty row in which we need to fill in the three cells Name, Short name and Quantity. <br>
We need to update the formulas for the newly created coin by: <br>
dragging down the values ​​formula by one
dragging down the total formula by one <br>
click on the pie chart and drag cell down for highlighted Short name and Value <br>
use a format painter for percent changes <br>

## The data is pulled from coinmarketcap.com using my private api key

