# a=[]
# n=4
# count=0
# for i in range(n):
#      a.append([])
#      for j in range(n):
#          a[i].append(int(input("Enter Numbers for Matrix ",i)))
#
# for i in a:
#     print(*i)

for i in range(5):
    for j in range(5):
        if (i+j==4):
            print(1)
        if (i+j==5):
            print(2)
        if (i+j==6):
            print(3)
        if (i+j==7):
            print(4)
        else:
            print('*')
    print()