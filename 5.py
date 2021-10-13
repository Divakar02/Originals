salary=int(input("Enter your salary: "))
pf=(7/100) * salary
hra=(5/100)*salary
da=(8/100) * salary
rent=(5/100) *salary
gross=(salary+da+rent-pf)
print(f"Basic Salary     :{int(salary)}")
print(f"PF               :{int(pf)}")
print(f"DearnessAllowance:{int(da)}")
print(f"Rent             :{int(rent)}")
print(f"Gross Salary     :{int(gross)}")