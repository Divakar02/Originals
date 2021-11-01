#2+22+222+2222
num=input("Enter the number: ")
terms=int(input("Number of terms in series: "))
# list=[]
# for i in range(1,terms+1):
#     a=int(num*i)
#     list.append(a)
# print(list)
#
# for i in list:
#     if i!=list[-1]:
#         print(f'{i}+',end='')
#     else:
#         print(f'{i}={sum(list)}')

count=0
for i in range(1,terms+1):
    a=int(num*i)
    count+=a
    if i<terms:
        print(f'{a}+',end='')
    else:
        print(f'{a}={count}', end='')





