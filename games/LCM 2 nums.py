# finding factors:

a=20
b=70

def factors(a):
    factors=[]
    for i in range(1,a):
        if a%i==0:
            factors.append(i)
    return factors

print(factors(a))
print(factors(b))