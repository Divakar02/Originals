bill=int(input("Enter the bill amount: "))

if bill>0 and bill<20000:
    billf = (bill/100) * 10
    disc=bill - billf
    print(f"Your final bill is {disc}")
elif bill>20001 and bill<30000:
    billf = (bill/100) * 20
    disc = bill - billf
    print(f"Your final bill is {disc}")
elif bill>30001 and bill<40000:
    billf = (bill/100) * 30
    disc = bill - billf
    print(f"Your final bill is {disc}")
elif bill>40001:
    billf = (bill/100) * 40
    disc = bill - billf
    print(f"Your final bill is {disc}")



