class Name:
    def __init__(self):
        self.fname = input("Enter ur first  name : ")
        self.lname = input("Enter ur second name : ")

class Mark(Name):
    def __init__(self):
        super().__init__()
        clas=int(input("Enter ur class: "))
        p6=int(input("Enter ur p6mrk: "))
        chem=int(input("Enter ur maths mrk: "))
        maths=int(input("Enter ur chem mrk: "))
        print(f'''
        Name : {self.fname} {self.lname}
        Class: {clas}
        P6   : {p6}
        Chem : {chem}
        Maths: {maths}''')
        if p6+chem+maths <150:
            print("Sry U failed!")
        else:
            print("Great u passed! ")

Mark()


