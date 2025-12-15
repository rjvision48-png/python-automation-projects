import pandas as pd
import os

def csv_data_cleaner():
    try:
        file_name = input("Enter CSV file name: ").strip()

        if not os.path.exists(file_name):
            print("File not found")
            return

        df = pd.read_csv(file_name)
        before = len(df)

        df = df.dropna()
        df = df.drop_duplicates()

        after = len(df)
        output = file_name.replace(".csv", "_cleaned.csv")
        df.to_csv(output, index=False)

        print("CSV cleaned successfully")
        print("Rows removed:", before - after)
        print("Saved as:", output)

    except Exception as e:
        print("Error:", e)

csv_data_cleaner()
