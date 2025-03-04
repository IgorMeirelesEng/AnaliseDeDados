import pandas as pd
df = pd.read_csv("supermarket_sales - Sheet1.csv")
def separate():
    print(100*"*")

print(df.info())
separate()
print(df.describe())
separate()
print(df.head())