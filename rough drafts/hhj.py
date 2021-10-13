m = int(input())
for i in range(0,m):
    for j in range(0,m):
        if i==m//2 or (i==0 and j!=0 and j!=m-1) or (j==0 and i!=0) or (j==m-1 and i!=0):
            print('*', end=' ')
        else:
            print(' ', end=' ')
    print()