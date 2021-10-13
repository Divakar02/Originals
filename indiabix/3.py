# list=[36, 34, 30, 28, 24,]
x=36
list=[x]
counter=0
while counter<=5:
    a=list[-1]-2
    list.append(a)
    b=a-4
    list.append(b)
    counter+=1
print(list)