num1=int(input())
num2=int(input())
list=[num1,num2]
max=int(max(list))
print(max)
j=1
for i in range(1,max):
    if (num1%i==0) and (i%num2%i==0):
        j*=i
    if not((num1%i==0) and (i%num2%i==0)):
        j
print(j)
