import csv

with open('Bill.csv','r') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        print(row[0])

with open('Bill.csv','a') as file2:
    writer=csv.writer(file)
