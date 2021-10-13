x=input("Enter the para: ")
a=[x]
X=a[0].split()
j=0
for i in X:
    if i==i[::-1]:
        print(i)
        j+=1

print(f"The number of palindrome is {j}")
