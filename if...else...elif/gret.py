x,y=int(input("Enter num1")),int(input("Enter num2"))

if (x%y)>(y%x):
    print(f"{y} is Greater")
elif (x%y)<(y%x):
    print(f"{x} is Greater")

print(x%y)
print(y%x)