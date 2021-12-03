y=[10,20,30,40,50]

import functools

b = functools.reduce(lambda a,b:a+b,y)
print(b)