import csv

with open('sample.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {row}')
            line_count += 1
        else:
            print(
                f'\t{row[1]} is {row[2]} years old, and is currently in semester {row[3]}.')
            line_count += 1
