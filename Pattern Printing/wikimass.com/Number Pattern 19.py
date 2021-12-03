'''
5      (5,6)
45     (4,6)
345    (3,6)
2345   (2,6)
12345  (1,6)
'''
# with string
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end='')
        if j==5:
            print(str(j)*(i-1))

#without string
for i in range(5,0,-1):
    for j in range(i,6):
        print(j,end='')
    for j in range(i-1):
        print(5,end='')
    print()


