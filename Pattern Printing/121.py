n=5

for i in range(1,6):
    for j in range(1,2*i):
        if i>j:
            print(j,end=' ')
        elif i<=j:
            x=(2*i)-j
            print(x,end=' ')
        else:
            print(" ",end=" ")
    print()