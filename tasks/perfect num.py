num = int(input("Enter num: "))
i=1
list=[]
while i<num:
    if num%i==0:
        list.append(i)
    i+=1
print(list)
if sum(list)==num:
    print(f'{num} is perfect number')
else:
    print(f'{num} is not perfect number')

