x= int(input("Enter: "))
square=str(x*x)
sum = 0
for i in str(square):
    sum +=int(i)

print(sum)

if sum==int(x):
    print(f'{x} is neon number')
else:
    print(f'{x} is not neon number')



