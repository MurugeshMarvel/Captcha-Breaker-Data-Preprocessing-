import csv

results = []

with open("ascii.csv") as f:
    reader = csv.reader(f)
    for row in reader:
        results.append(row)

print(results)
