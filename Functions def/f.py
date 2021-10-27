
# A is father of B but B is not son of A how?
#
# string=input("Enter the string: ")
# positions=int(input("Enter the num of positions to rotate: "))
# if positions<len(string):
#     final=string[positions::]+string[0:positions]
# else:
#     final=string+" position exceeds length"
#     print(final)

import csv

F=open("C:\\Users\Divakar\Desktop\sample.csv","r")
row=csv.reader(F)
for i in row:
    print(i)
