import psycopg2
import pandas as pd

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
    print("Successfully connected.")
except Exception as e:
    print(f"Connection error. Error: {e}")

cur = conn.cursor()


def create_table():
    cur.execute("""
                            CREATE TABLE GOOGLE_PLAY(
                            ID SERIAL PRIMARY KEY,
                            App TEXT NOT NULL,
                            Category TEXT NOT NULL,
                            Rating FLOAT,
                            Reviews INT,
                            Size_mb INT,
                            Installs_plus INT,
                            Type TEXT,
                            Price_$ FLOAT,
                            Content_Rating TEXT,
                            Genres TEXT)""")
    conn.commit()
    print("Table created successfuly")


def create_tuples():
    data_tuples = ()
    df = pd.read_csv("prepared_data.csv")
    for i, row in df.iterrows():
        data_list = []
        data_list.append(row['App'])
        data_list.append(row['Category'])
        data_list.append(row['Rating'])
        data_list.append(row['Reviews'])
        data_list.append(row['Size'])
        data_list.append(row['Installs'])
        data_list.append(row['Type'])
        data_list.append(row['Price'])
        data_list.append(row['Content Rating'])
        data_list.append(row['Genres'])
        data_list = tuple(data_list)
        data_tuples += (data_list,)
    return data_tuples


def insert_many(data):
    query = """INSERT INTO GOOGLE_PLAY (App, Category, Rating, Reviews, Size_mb, Installs_plus, Type, 
            Price_$, Content_Rating, Genres)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    cur.executemany(query, data)
    conn.commit()
    print("Many rows inserted successfuly")


def chunks(data, divider):
    """Yield n number of striped chunks from l."""
    for i in range(0, divider):
        yield data[i::divider]


def find_duplicates():
    """Provides number of unique data rows from 10840 record"""
    cur.execute("SELECT DISTINCT ON (app) * FROM GOOGLE_PLAY;")
    rows = cur.fetchall()
    print(len(rows))


def remove_duplicates():
    """Removes duplicates from Database"""
    cur.execute("DELETE FROM "
                "    GOOGLE_PLAY a "
                "        USING GOOGLE_PLAY b "
                "WHERE "
                "    a.id < b.id "
                "    AND a.app = b.app;")
    conn.commit()


create_table()

data_prepared = create_tuples()
# creates a single tuple for each row

bites = chunks(data_prepared, 542)
# chunks data (542 small pieces)

for b in bites:
    try:
        insert_many(b)
    except Exception as e:
        print(f"I was to unable do that. {e} ")
    else:
        pass
# Inserts the data to database

find_duplicates()
remove_duplicates()
conn.close()
# removes duplicates and closes connection
