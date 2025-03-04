import sqlite3
import pandas as pd
df = pd.read_csv("supermarket_sales - Sheet1.csv")

con = sqlite3.connect("sales.db")
df.to_sql("sales", con, if_exists="replace", index=False)