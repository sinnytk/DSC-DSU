import csv

with open('sample.csv', mode='r') as friends:
    friends_reader = csv.DictReader(friends)
    for friend in friends_reader:
        print(friend["Name"])
