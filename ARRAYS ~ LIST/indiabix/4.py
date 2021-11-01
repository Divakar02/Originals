# 22, 21, 23, 22, 24, 23,

x=22
list=[x]
counter=0
while counter<=5:
    a=list[-1]-1
    list.append(a)
    b=a+2
    list.append(b)
    counter+=1
print(list)