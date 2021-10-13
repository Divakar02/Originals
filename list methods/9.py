n=int(input("Enter the number: "))
x=n
c=1
while True:
    x=x//10
    c += 1
    if x<10:
        break
print(f"It has {c} digits")

