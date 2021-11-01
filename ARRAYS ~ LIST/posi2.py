listA=[0,1,2,3,4,5,6,7,8,9]
listB=['a','b','c','d','e','f','g','h','i','j']
# listUnion=[1,a,2,b,3,c,4,d,5,e,6,f,7,g,8,h,9,i,j,10]

for i in range(10):
    listA.insert(listA[i+i], listB[i])

print(listA)
