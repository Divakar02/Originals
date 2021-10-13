list=["Emmy","John","","Kelly",None,"Eric"]
listf=[]
for i in list:
    if i!="" and i!=None:
        listf.append(i)
print('Original List\n',list)
print('After removing\n',listf)