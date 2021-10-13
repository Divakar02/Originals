a=[1,2,2,4,5,6,6,6,6]

listA=[]

for i in range(8):
    if a[i]==a[(i+1)]:
        z=(a[i],a[i]+1)
        listA.extend(z)
        if a[i] == a[(i + 2)]:
            z = (a[i], a[i] + 2)
            listA.extend(z)
            if a[i] == a[(i + 3)]:
                z = (a[i], a[i] + 3)
                listA.extend(z)



print(listA)

