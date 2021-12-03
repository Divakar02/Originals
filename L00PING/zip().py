import random

a=[i for i in range(100)]
b=[-1*i for i in range(100)]

check=a+b
print(check)
lst=[]
for x in check:
    for y in check:

        if (x*x)/16 - (y*y)/64 ==1:
            print(x, y, sep=' and ',end=' ')
            print('possible !!')
            lst.extend([[x, y]])
        else:
            print(x, y, sep=' and ')
print(lst)