import pandas as pd

df = pd.read_excel("data.xlsx")
summary = df.describe()
summary.to_excel("report.xlsx")
