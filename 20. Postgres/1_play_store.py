import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)
pd.set_option('display.width', 800)
# setting display options


df = pd.read_csv("googleplaystore.csv")

# loading data


df = df.drop([df.index[10472]])
df["Reviews"] = pd.to_numeric(df["Reviews"])
# ----------------Reviews corrected and changed to int

# df["Rating"]=df["Rating"].fillna("")
# df["Rating"] = pd.to_numeric(df["Rating"])
# print(df["Rating"])
# ----------------Not needed to be done

for i, row in df.iterrows():
    if row["Size"][-1] == "k":
        new = row["Size"][:-1]
        new = float(new)
        df.at[i, 'Size'] = new
    elif "Varies" in row["Size"]:
        new = 0.0
        df.at[i, 'Size'] = new
df['Size'] = df['Size'].str.rstrip('M')
df["Size"] = pd.to_numeric(df["Size"])
# ----------------Size corrected and changed to float

df['Price'] = df['Price'].str.lstrip('$')
df["Price"] = pd.to_numeric(df["Price"])
# ----------------Price corrected and changed to float

df['Installs'] = df['Installs'].str.rstrip('+')
df['Installs'] = df['Installs'].apply(lambda x: x.replace(",", ""))
df["Installs"] = pd.to_numeric(df["Installs"])
# ----------------Installs corrected and changed to int

df['Genres'] = df['Genres'].apply(lambda x: x.replace(";", ", "))
# ----------------Some genres had ; istead , replaced (Action;Action & Adventure)--->(Action, Action & Adventure)


print(df)
print(df.dtypes)
df.to_csv("prepared_data.csv")
