for i in range(6,0,-1):
    if (i%2==0):
        for j in range(1,i):
            print(j,end='')
    else:
        for j in range(i-1,0,-1):
            print(j,end='')
    print()
'''
i=6 (1,6)     
i=5 (4,0,-1)
i=4 (1,4)
i=3 (2,0,-1)
i=2 (1,2)
'''