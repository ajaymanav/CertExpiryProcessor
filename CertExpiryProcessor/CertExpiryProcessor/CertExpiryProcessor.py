import os
import pandas as pd
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_DIR, 'data.csv')

def process_csv():
    print("CsvExpiryProcessor started...")

    try:
        df = pd.read_csv(CSV_FILE)
    except FileNotFoundError:
        print("❌ CSV file not found.")
        return
    except Exception as e:
        print(f"❌ Failed to read CSV: {e}")
        return

    today = datetime.today()

    for index, row in df.iterrows():
        try:
            expiry_date = datetime.strptime(row['expirydate'], "%Y-%m-%d")
            days_until_expiry = (expiry_date - today).days
            if 0 <= days_until_expiry <= 30:
                print(f"Extending expiry for {row['name']} from {row['expirydate']}")
                new_expiry = expiry_date + timedelta(days=365)
                df.at[index, 'expirydate'] = new_expiry.strftime("%Y-%m-%d")
        except Exception as e:
            print(f"⚠️ Error processing row {index}: {e}")

    try:
        df.to_csv(CSV_FILE, index=False)
        print("CsvExpiryProcessor completed.")
    except Exception as e:
        print(f"❌ Failed to write CSV: {e}")

if __name__ == "__main__":
    process_csv()
