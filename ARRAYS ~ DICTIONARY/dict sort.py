dictnew={'a':"Hello",
      "b":"1",
      'c':'Jayaltha',
      'd':[1,2]}

dictfinal={}
values=sorted(list(dictnew.values()),key=len)

for i in values:
    for j,k in dictnew.items():
        if(i==k):
            dictfinal[j]=i

print(dictfinal)


