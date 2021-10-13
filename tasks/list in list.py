list=[5,913,423,53,235,32,22,33,49,96]



diff=0


while diff>0:
    for i in range(len(list)):
        if list[i] != list[-1]:
            if list[i] < list[i + 1]:
                list[i], list[i + 1] = list[i + 1], list[i]
        if list[i] == list[-1]:
            for i in range(len(list)):
                z=x[i]-x[i+1]
                diff+=z

print(diff)
print(list)
print(list[::-1])




