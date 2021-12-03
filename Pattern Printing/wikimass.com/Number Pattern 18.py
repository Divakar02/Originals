for i in range(5,11):
    if i%2!=0:
        for j in range(1,i,2):
            print(j,end='')
    else:
        for j in range(2,i+1,2):
            print(j,end='')
    print()

for i in range(2,6,2):
    print(i)
'''
(1,2) odd
(2,6,2) even
(1,7,2) odd
(2,9,2) even
(1,10,2) odd
'''