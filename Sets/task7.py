set1={10,20,30,40,50}
set2={30,40,50,60,70}
x=set1.difference(set2)
for i in x:
    set1.remove(i)
print(set1)
