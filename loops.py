#+3 -2
list=[7,10,8,11,9,12]
for i in list:
    if i <20:
        a=list[-1]-2
        list.append(a)
        b=a+3
        list.append(b)
print(list)

