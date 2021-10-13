A=[]
even=[]
odd=[]
for i in range(5):
    x=int(input())
    A.append(x)
    # if x%2==0:
    #     even.append(x)
    # else:
    #     odd.append(x)
for i in A:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print('Actual list: ',A)
print('Even List: ',even)
print('Odd List: ',odd)
even.extend(odd)
print(sorted(even))

