x=int(input("Enter num1: "))
y=int(input("Enter num2: "))
#1digit
if x>0 and x<10:
    a=1
if y>0 and y<10:
    b=1
#2digit
if x>9 and x<100:
    a=2
if y>9 and y<100:
    b=2
#3digit
if x>99 and x<1000:
    a=3
if y>99 and y<1000:
    b=3
#if>3digit
if x>999 or y>999:
    print("INVALID! ")

if a==b:
    print(x+y)
elif a!=b:
    print(x-y)
