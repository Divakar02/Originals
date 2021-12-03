l=[i for i in range(1,10)]
def even(i):
    return i%2==0
def doubles(i):
    return i**2
a=list(filter(doubles,l))
print(a)


# ___

a=[str(i) for i in range(10)]

b=list(map(lambda x:int(x),a))