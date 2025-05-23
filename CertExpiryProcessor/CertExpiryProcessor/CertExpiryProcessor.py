import os
import csv
from datetime import datetime, timedelta

BASE_DIR = os.path.dirname(__file__)
CSV_FILE = os.path.join(BASE_DIR, 'data.csv')

def process_csv():
    print("CsvExpiryProcessor started...")

    updated_rows = []
    today = datetime.today()

    with open(CSV_FILE, mode='r', newline='') as infile:
        reader = csv.DictReader(infile)
        for row in reader:
            expiry_date = datetime.strptime(row['expirydate'], "%Y-%m-%d")
            if 0 <= (expiry_date - today).days <= 30:
                print(f"Extending expiry for {row['name']} from {row['expirydate']}")
                expiry_date += timedelta(days=365)
                row['expirydate'] = expiry_date.strftime("%Y-%m-%d")
            updated_rows.append(row)

    with open(CSV_FILE, mode='w', newline='') as outfile:
        writer = csv.DictWriter(outfile, fieldnames=['name', 'expirydate'])
        writer.writeheader()
        writer.writerows(updated_rows)

    print("CsvExpiryProcessor completed.")


if __name__ == "__main__":
    process_csv()

