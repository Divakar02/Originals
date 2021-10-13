import math
x=int(input("Enter the num: "))
list=[x]
# x!=4*3*2*1=24
i=1

while i<x:
    x=list[-1]-1
    list.append(x)
print(math.prod(list))

