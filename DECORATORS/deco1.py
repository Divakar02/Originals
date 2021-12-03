def strupr(func):
    def inner():
        str1=func()
        return str1.upper()
    return inner
# @strupr
def printstr():
    return "gud morning"

print(printstr())
# d=strupr(printstr)
# print(d())