a=int(input("Enter the year: "))
if a%100==0:
    if a%400==0:
        print("Its leap year")
    else:
        print("Its not leap year")
elif a%4==0:
    print(f"{a} is leap year")
elif a%4!=0:
    print(f"{a} is not leap year")