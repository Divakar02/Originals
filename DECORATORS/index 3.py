def outer():
    x=3
    def inner():
        y=3
        res=x+y
        return res
    def inner2():
        y = 4
        res = x + y
        return res
    def inner3():
        y = 5
        res = x + y
        return res
    return inner2

a=outer()
print(a())
print(a.__name__)
