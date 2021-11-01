# 2, 1, (1 / 2), (1 / 4)
x=float(input("Enter: "))
list=[x]
i=0

while i<=5:
    a=list[-1]/2
    list.append(a)
    i+=1

print(list)
print(len(list))

