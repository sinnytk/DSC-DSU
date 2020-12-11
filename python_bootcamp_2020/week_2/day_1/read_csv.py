import csv

with open("sample.csv") as sample_file:
    reader = csv.reader(sample_file)
    for row in reader:
        print(row)
