# program to find even nos:

l=[1,2,3,4,5,6,7,8]

def even(i):
    return i%2==0

a=list(filter(even,l))

# using lambda

b=list(filter(lambda x:x%2==0,l))

print('''
         ^  ^
        (.)(.)
          ()
        ______
        |    |
        |    |
        |    |
        ______
        ||  ||
        ||  ||
         ''')
        ___ ___


