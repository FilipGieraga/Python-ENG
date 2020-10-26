# Program Corporate structure:

Requirements: Python 3, pandas, psycopg2, tkinter

## Documentation:

This program was about creating a graphical interface for a database hosted on https://api.elephantsql.com/.
It consists of three parts, where the first one focuses on converting data from kaggle.com
(source: https://www.kaggle.com/lava18/google-play-store-apps?select=googleplaystore.csv)
to values that allow us to send queries, i.e.:
- Reviews - string to int
- Size - string to float
- Installs - string to int
- Price - string to float<br>

After conversion, second part of this project inputs data into database using
a generator which divides it into bites and gets rid of duplicates.<br>
The third part is creating an interface using the tkinter library and allowing user to send queries.<br>
Here are queries that you can send to db:
- fetch_all() - Fetches all data with limit allowance
- rating_by_category() - Average rating of all categories descending where rating!=NaN
- app_count_in_category() - App counter for each Category descending
- best_app_in_category() - Apps with more than 10000 installs and rating more equal 4.8
- most_downloaded_apps() - Most downloaded apps in store with limit allowance
- dynamic_query_category_rating() - Apps from Category provided in dropbox with rating more equal to the one given in field with limit allowance
- most_expensive_apps() - Most expensive apps descendign with limit allowance
- app_finder() - App finder looking for partial or complete match in App name field

## Disclaimer
I didn't want data to by amended, that's why credentials to my db are not in the code.<br>
You can query data with GUI

![alt tag](https://github.com/FilipGieraga/Python-ENG/blob/master/20.%20Postgres/gui_pic.PNG)

