from tkinter import *
import tkinter.font as font
import psycopg2

DB_NAME = "##########"
DB_USER = "##########"
DB_PASS = "##########"
DB_HOST = "##########"
DB_PORT = "##########"

try:
    conn = psycopg2.connect(database=DB_NAME,
                            user=DB_USER,
                            password=DB_PASS,
                            host=DB_HOST,
                            port=DB_PORT)
    print("Database connected")
except Exception as e:
    print(f"Connection error. Error: {e}")

cur = conn.cursor()


def fetch_all():
    """Fetch all data and allow to limit to specific number"""
    global l2, limit
    query_limit = limit.get()
    try:
        query_limit = int(query_limit)
    except:
        query_limit = ""
    l2.configure(text="ID | App_name | Categrory | Rating | Reviews | Size MB | Installs_plus | Type | Price($) | "
                      "Content Rating | Genre(s)")
    output_data.delete(0, END)
    cur.execute("SELECT * from google_play;")
    rows = cur.fetchall()
    if isinstance(query_limit, int):
        for row in rows[:query_limit]:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |"
                                    f" {row[7]} | {row[8]} | {row[9]} | {row[10]}")
    else:
        for row in rows:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |"
                                    f" {row[7]} | {row[8]} | {row[9]} | {row[10]}")


def rating_by_category():
    """Average rating of all categories descending where rating!=NaN"""
    global l2
    output_data.delete(0, END)
    l2.configure(text="Category | Average Rating")
    cur.execute("SELECT category, AVG(rating) FROM google_play gp "
                "WHERE gp.rating != 'nan' "
                "GROUP BY gp.category "
                "ORDER BY AVG(rating) desc;")
    rows = cur.fetchall()
    for row in rows:
        rating = float(row[1])
        rating = round(rating, 2)
        equal_string = str(row[0])
        output_data.insert(END, f"{equal_string} | {rating}")


def app_count_in_category():
    """App counter for each Category descending"""
    output_data.delete(0, END)
    l2.configure(text="Category | Counter")
    cur.execute("SELECT CATEGORY, COUNT(APP) AS COUNTER FROM GOOGLE_PLAY "
                "GROUP BY CATEGORY "
                "ORDER BY COUNTER DESC;")

    rows = cur.fetchall()
    for row in rows:
        output_data.insert(END, f"{row[0]} | {row[1]}")


def best_app_in_category():
    """Apps with more than 10000 installs and rating more equal 4.8"""
    global l2
    output_data.delete(0, END)
    l2.configure(text="App | Category | Rating | Type | Content Rating")
    cur.execute("SELECT APP, CATEGORY, RATING, TYPE, Content_rating FROM GOOGLE_PLAY "
                "WHERE rating != 'nan' AND rating >= 4.8  And Installs_plus > 10000 "
                "ORDER BY Category;")

    rows = cur.fetchall()
    for row in rows:
        output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]}")


def most_downloaded_apps():
    """Most downloaded apps in store with limit allowance"""
    global l2, limit
    query_limit = limit.get()
    try:
        query_limit = int(query_limit)
    except:
        query_limit = ""
    output_data.delete(0, END)
    l2.configure(text="App | Category | Installs_plus")
    cur.execute("SELECT app, category ,installs_plus from google_play "
                "ORDER BY installs_plus desc;")
    rows = cur.fetchall()
    if isinstance(query_limit, int):
        for row in rows[:query_limit]:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]}")
    else:
        for row in rows:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]}")


def dynamic_query_category_rating():
    """Apps from Category provided in dropbox with rating more equal to the one given in field with limit allowance"""
    global l2, limit, rating, variable, l6
    query_limit = limit.get()
    query_rating = rating.get()
    try:
        query_limit = int(query_limit)
    except:
        query_limit = ""
    try:
        query_rating = float(query_rating)
        query_rating = str(query_rating)
    except:
        return l6.configure(text="Please use int or float for rating and int for limit")
    cat = variable.get()
    output_data.delete(0, END)
    l6.configure(text="")
    l2.configure(text="App | Rating | Type | Installs_plus")
    cur.execute("SELECT APP, RATING, TYPE, Installs_plus  FROM GOOGLE_PLAY "
                "WHERE CATEGORY = %s AND RATING != 'nan' AND RATING >= %s "
                "ORDER BY APP;", (cat, query_rating))
    rows = cur.fetchall()
    if isinstance(query_limit, int):
        for row in rows[:query_limit]:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    else:
        for row in rows:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")


def most_expensive_apps():
    """Most expensive apps with limit allowance"""
    global l2, limit
    query_limit = limit.get()
    try:
        query_limit = int(query_limit)
    except:
        query_limit = ""
    output_data.delete(0, END)
    l2.configure(text="App | Category | Prize($)")
    cur.execute("SELECT app, category , price_$ from google_play "
                "WHERE price_$> 0 "
                "ORDER BY price_$ desc;")
    rows = cur.fetchall()
    if isinstance(query_limit, int):
        for row in rows[:query_limit]:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]}")
    else:
        for row in rows:
            output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]}")


def app_finder():
    """App finder looking for partial or complete match in App name field"""
    global l2, app_name
    name = app_name.get()
    new_name = "%" + name + "%"
    l2.configure(text="ID | App_name | Categrory | Rating | Reviews | Size MB | Installs_plus | Type | Price($) | "
                      "Content Rating | Genre(s)")
    output_data.delete(0, END)
    cur.execute("SELECT * from google_play "
                "WHERE LOWER(App) LIKE %s ;", [new_name])
    rows = cur.fetchall()
    for row in rows:
        output_data.insert(END, f"{row[0]} | {row[1]} | {row[2]} | {row[3]} | {row[4]} | {row[5]} | {row[6]} |"
                                f" {row[7]} | {row[8]} | {row[9]} | {row[10]}")


window = Tk()
window.wm_title("Database access")
w, h = window.winfo_screenwidth(), window.winfo_screenheight()
window.geometry("%dx%d+0+0" % (w, h))

# Labels

myfont = font.Font(weight="bold", size=14)

l1 = Label(window, text="Data from Postgres:")
l1["font"] = myfont
l1.grid(row=0, column=4)

l2 = Label(window, text="Column names")
l2.grid(row=1, column=1)

l3 = Label(window, text="1. Category")
l3.grid(row=5, column=11, ipadx=30)

l4 = Label(window, text="2. Limit")
l4.grid(row=6, column=11)

l5 = Label(window, text="3. Rating")
l5.grid(row=7, column=11)

l6 = Label(window, text="")
l6.grid(row=9, column=12)

l7 = Label(window, text="4. App name")
l7.grid(row=8, column=11)

# Listbox
output_data = Listbox(window, height=40, width=150)
output_data.grid(row=2, column=1, rowspan=15, columnspan=8, sticky="news")

# Scrollbar
scrollbar = Scrollbar(window, orient='vertical', command=output_data.yview)
scrollbar.grid(row=3, column=8, sticky='ens', rowspan=13)
output_data.config(yscrollcommand=scrollbar.set)
# Input text

limit = Entry(window, width=10)
limit.grid(row=6, column=12)

rating = Entry(window, width=10)
rating.grid(row=7, column=12)

app_name = Entry(window, width=10)
app_name.grid(row=8, column=12)

# Buttons

b1 = Button(window, text="View all - 2", width=20, command=fetch_all)
b1.grid(row=3, column=10)

b2 = Button(window, text="Rating by Category", width=20, command=rating_by_category)
b2.grid(row=4, column=10)

b3 = Button(window, text="Best Apps in Categories", width=20, command=best_app_in_category)
b3.grid(row=5, column=10)

b4 = Button(window, text="App Count in Categories", width=20, command=app_count_in_category)
b4.grid(row=6, column=10)

b5 = Button(window, text="Most Downloaded Apps - 2", width=20, command=most_downloaded_apps)
b5.grid(row=7, column=10)

b6 = Button(window, text="Dynamic Query - 1 & 2 & 3", width=20, command=dynamic_query_category_rating)
b6.grid(row=8, column=10)

b7 = Button(window, text="App Finder - 4", width=20, command=app_finder)
b7.grid(row=9, column=10)

b8 = Button(window, text="Most Expensive Apps - 2", width=20, command=most_expensive_apps)
b8.grid(row=10, column=10)

# dropdown
variable = StringVar(window)
variable.set("ART_AND_DESIGN")  # default value
drop_down = OptionMenu(window, variable, 'ART_AND_DESIGN', 'AUTO_AND_VEHICLES', 'BEAUTY', 'BOOKS_AND_REFERENCE',
                       'BUSINESS', 'COMICS', 'COMMUNICATION', 'DATING', 'EDUCATION', 'ENTERTAINMENT', 'EVENTS',
                       'FINANCE', 'FOOD_AND_DRINK', 'HEALTH_AND_FITNESS', 'HOUSE_AND_HOME', 'LIBRARIES_AND_DEMO',
                       'LIFESTYLE', 'GAME', 'FAMILY', 'MEDICAL', 'SOCIAL', 'SHOPPING', 'PHOTOGRAPHY', 'SPORTS',
                       'TRAVEL_AND_LOCAL', 'TOOLS', 'PERSONALIZATION', 'PRODUCTIVITY', 'PARENTING', 'WEATHER',
                       'VIDEO_PLAYERS', 'NEWS_AND_MAGAZINES', 'MAPS_AND_NAVIGATION')

drop_down.grid(row=5, column=12)

window.mainloop()
