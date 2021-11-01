x=input()

count=1

for i in range(len(x)-1):
    if x[i]==x[i+1]:
        count+=1
    else:
        print(f'{x[i]}{count}',end='')
        # del(count)
        count=1

print(f'{x[i]}{count}')