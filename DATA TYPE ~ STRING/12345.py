n=int(input())
start=n
sum=0
for i in range(n,0,-1):
    if i!=1:
        print(i,end='+')
        sum+=i
    else:
        sum += i
        print(i,end=f'={sum}',)



