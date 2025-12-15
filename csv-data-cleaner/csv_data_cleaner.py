import pandas as pd
import os

def csv_data_cleaner():
    try:
        print("=== CSV DATA CLEANER ===\n")

        # -------- INPUT --------
        file_name = input("Enter CSV file name (example: data.csv): ").strip()

        if not os.path.exists(file_name):
            print("File not found. Please check the file name.")
            return

        # -------- READ CSV --------
        df = pd.read_csv(file_name)
        original_rows = len(df)

        print(f"\nOriginal rows: {original_rows}")
        print(f"Columns found: {list(df.columns)}")

        # -------- CLEANING --------
        df = df.dropna()
        df = df.drop_duplicates()

        cleaned_rows = len(df)
        removed_rows = original_rows - cleaned_rows

        # -------- OUTPUT --------
        output_file = file_name.replace(".csv", "_cleaned.csv")
        df.to_csv(output_file, index=False)

        # -------- RESULT --------
        print("\nCSV cleaning completed successfully")
        print(f"Rows removed: {removed_rows}")
        print(f"Final rows: {cleaned_rows}")
        print(f"Cleaned file saved as: {output_file}")

    except pd.errors.EmptyDataError:
        print("The CSV file is empty.")

    except Exception as e:
        print("An unexpected error occurred:", e)


# -------- RUN SCRIPT --------
csv_data_cleaner()
