x=int(input("Enter the number: "))
listA=[]
for i in str(x):
    listA.append(int(i))
listB=[]
for j in listA:
    m=j**len(str(x))
    listB.append(int(m))
final=sum(listB)
print(final)