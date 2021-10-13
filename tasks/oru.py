# # start=int(input('start= '))[0]
# # end=start[-1]
# # j=0
# # for i in range(start,end+1):
# #     if i<end:
# #         print(i,end='+')
# #         j+=i
# #     elif i==end:
# #         print(i, end='')
# #         j += i
# #         print(f'={j}')
# #
# # 123
# # 1+2+3=sum[int(d) for d in str(n)]
# n=int(input("Enter number: "))
# list=[int(d) for d in str(n)]
# for i in list:

#     print(i,end='')

num=int(input("Enter num: "))
factorial=0
j=0
for i in range(1,num + 1):
    if i<num:
        factorial = factorial+i
        print(i,end='+')
        j+=i
    else:
        print(i,end='')
        j+=i
        print(f'={j}',end='')

