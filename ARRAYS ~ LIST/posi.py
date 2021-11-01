# A=54321
# B=5+4+3+2+1=15
num=int(input("Enter num: "))
list=[]

for i in range(5,0,-1):
    if i>1:
        print(i,end='+')
        list.append(i)
    elif i==1:
        list.append(i)
        print(f"{i}={sum(list)}")

