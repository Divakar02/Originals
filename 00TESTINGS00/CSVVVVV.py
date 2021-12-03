import csv

# csv.register_dialect('dummy',delimiter=',',quoting=csv.QUOTE_ALL,skipinitialspace=True)

f=open("file123.csv",'r')
reader=csv.reader(f)
for i in reader:
    print(i)

f.close()