n=int(input("enter num: "))

count=1

while True:
    if n//10>0:
        n=n//10
        count+=1
    else:
        break

print(count)

