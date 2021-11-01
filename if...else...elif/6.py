x=str(input("Enter number1: "))
y=str(input("Enter number2: "))
if len(x)==len(y):
    print(int(x)+int(y))
elif len(x)!=len(y):
    print(int(x)-int(y))