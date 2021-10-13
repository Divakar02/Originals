a=[1,2,2,4,5,6,6,6]
b=[]
for i in range(1,len(a)+1):
    if(a[i-1] == i):
        pass
    else:
        b.append(a[i-1])
        b.append(i)
print(b)



