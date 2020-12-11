import csv

with open('sample.csv', mode='a') as friends:
    friends_writer = csv.DictWriter(
        friends, fieldnames=["", "Name", "Age", "Semester"])
    friends_writer.writerow(
        {"Age": "30", "Name": "Zaid Bin Harris", "Semester": "10"})
