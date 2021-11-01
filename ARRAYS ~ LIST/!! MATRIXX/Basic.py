a=[]
n=4
count=0
for i in range (n):
     a.append([])
     for j in range(n):
         a[i].append(int(input("enter num")))
         if(i+j==n-1):
          count+=a[i][j]


for i in a:
    print(*i)

