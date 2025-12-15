import pandas as pd

file = input("Enter Excel file name: ")
df = pd.read_excel(file)

print("Columns:", df.columns.tolist())
print("Rows:", len(df))
