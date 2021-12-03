# class Demo:
#     def __init__(self,vari):
#         print("halo world",vari)
#
# Demo('hai')

# class A:
#     def __init__(self):
#         print("A is class")
# class B(A):
#     def __init__(self):
#         print("B is class")
#         super().__init__()
#
# obj=B()


class Student:
    def __init__(self,name,sec,roll):
        self.name=name
        self.sec=sec
        self.roll=roll

s1=Student("Ram","A1","1")
s2=Student("Sam","A2",2)
print(s2.name)