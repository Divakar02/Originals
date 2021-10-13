a=int(input("Enter num1: "))
b=int(input("Enter num2: "))
c=int(input("Enter num3: "))

d=a+b
e=b+c
f=c+a
g=a&b
h=b&c
i=c&a

z=[a,b,c,d,e,f,g,h,i]


print('Greatest is:',max(z))
z.sort()
print("Ascending order: ",z)s
z.sort(reverse=True)
print("Descending order: ",z1)