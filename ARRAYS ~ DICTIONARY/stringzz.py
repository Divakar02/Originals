string='oceanacademjjjjjjjjjjy'
dict1={}
list1=[]

for i in string:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1

for i,j in dict1.items():
    print(i,j)
# largest = list(dict1.values())
# print(largest)
# for i,j in dict1.items():
#     if max(largest)==j:
#         print(f'The letter \'{i}\' has max value as {j}')

#without functions:
# for b in range(len(list)):
#     for i in range(len(list)-1):
#         if list[i]>list[i+1]:
#             list[i],list[i+1]=list[i+1],list[i]
# for i,j in dict.items():
#     if list[::-1}==j:
#         print(f'The letter \'{i}\' has max value as {j}')