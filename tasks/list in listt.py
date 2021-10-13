L1=[]
L2=[]
for i in range(4):
    x = int(input("Enter num: "))
    if i<2:
        L1.append(x)
    else:
        L2.append(x)
LF=[]
LF.append(L1)
LF.append(L2)
print(LF)
