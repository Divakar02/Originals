# # 1,2,3,5,8,13,21
#
# list=[0]
# inpt=int(input())
# for i in range(inpt+1):
#     if len(list)==1:
#         j=list[-1]+1
#         list.append(j)
#     else:
#         j=list[-1]+list[-2]
#         list.append(j)
# print(list)
# print(f'The {inpt}th term is {list[inpt-1]}')
def feb(y):
 n=int(y)
 if n==1:
  return 0
 elif n==2:
  return 1
 else:
  x=feb(n-1)+feb(n-2)
  return x
print(feb(5))