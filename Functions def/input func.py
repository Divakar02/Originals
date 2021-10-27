# def inputt():
#     global a
#     a=int(input("Enter num: "))
#     square()
#     cube()
# def square():
#     print(a**2)
# def cube():
#     print(a**3)
# inputt()


def inputt():
    global a, b, c, d
    a,b,c,d=int(input("Enter num1: ")),int(input("Enter num2: ")),int(input("Enter num3: ")),int(input("Enter num4: "))
    multiply()
    divide()
    print(float(multi)+float(divi))
def multiply():
    global multi
    multi=a*b
    print(a*b)
def divide():
    global divi
    divi=c/d
    print(c/d)
inputt()