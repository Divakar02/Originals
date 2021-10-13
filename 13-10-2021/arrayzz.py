#swappin arrays
a=[1,4,20,2]
b=[5,9,6,3]
count=0
if sum(a)%2!=0 or sum(b)%2!=0:
    for i in range(max(len(a),len(b))):
        x=a[i]
        a[i]=b[i]
        b[i]=x
        print(f"{a[i]} of array1 is swapped with {b[i]} of array2")
        if sum(a)%2==0 and sum(b)%2==0:
            break

print(count)
