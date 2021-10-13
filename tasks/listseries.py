# list=[7,10,8,11,9,12]
x=int(input("Enter: "))
list=[x]
counter=0
if x%10!=0:
    while counter<=5:
        a=list[-1]+3
        list.append(a)
        b=a-2
        list.append(b)
        counter+=1
else:
    while counter<=5:
        a=list[-1]-2
        list.append(a)
        b=a+3
        list.append(b)
        counter+=1
print(list)
print(len(list))

