import csv

with open ('/Users/ashishjhade/Documents/myCode/data/weight-height.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter = ',')
