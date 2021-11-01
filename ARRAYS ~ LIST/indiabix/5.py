# 53, 53, 40, 40, 27, 27,

x=53
list=[x]
counter=0
while counter<=5:
    a=list[-1]-13
    list.append(a)
    list.append(a)
    counter+=1
print(list)