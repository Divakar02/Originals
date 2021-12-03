print(dir())

num=20

def f1():
    n=10
    print("inside",dir())
f1()
print("outside",dir())
