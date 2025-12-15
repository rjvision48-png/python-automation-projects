import pandas as pd

df = pd.read_csv("data.csv")
df = df.dropna().drop_duplicates()
df.to_excel("cleaned.xlsx", index=False)
