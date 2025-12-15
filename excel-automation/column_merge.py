import pandas as pd

df = pd.read_excel("data.xlsx")
df["Merged"] = df["Column1"].astype(str) + " " + df["Column2"].astype(str)
df.to_excel("merged.xlsx", index=False)
