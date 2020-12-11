import csv

with open('sample.csv', mode='a') as friends:
    friends_writer = csv.writer(friends, delimiter=',')

    friends_writer.writerow(['', 'Hamza Fayyaz', '22', '7'])
    friends_writer.writerow(['', 'Syed Ali', '25', '7'])
