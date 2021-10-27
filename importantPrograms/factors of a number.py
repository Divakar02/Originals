# finding factors:

a=20
factors=[]
for i in range(1,a+1):
    if a%i==0:
        factors.append(i)

print(factors)