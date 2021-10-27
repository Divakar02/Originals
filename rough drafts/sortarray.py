x = list(map(int, input("Enter comma separated values: ").split(",")))
print('Given Numbers    =>',x)
# greater swap
for b in range(len(x)):
    for i in range(len(x)-1):
        if x[i]>x[i+1]:
            x[i],x[i+1]=x[i+1],x[i]

print('Ascending Order  =>',x)
print('Descending Order =>',x[::-1])
