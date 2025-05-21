import csv
import json

with open('data.csv', 'r') as f:
    reader = csv.DictReader(f)
    rows = list(reader)

with open('data.json', 'w') as f:
    json.dump(rows, f, indent=4)
print("CSV data has been converted to JSON format.")