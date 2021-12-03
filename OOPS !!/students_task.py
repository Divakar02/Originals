class Employee:
    def INPUT():
        fname=input("Enter first name: ")
        lname=input("Enter last name: ")


class Salary():
    def SALARY():
        house_rent=int(input("Enter house rent: "))
        pf=int(input("Enter pf amount: "))
        loan=int(input("Enter loan amount: "))
        print(f'''
        Name  : {fname} {lname}
        Rent  : {house_rent}
        pf    : {pf}
        Loan  : {loan}
        Salary: {(house_rent + pf + loan)/2}''')

Employee.INPUT()
Salary.SALARY()
