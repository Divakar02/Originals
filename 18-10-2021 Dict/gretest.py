#method-1
x=[]
for i in range(6):
    y=int(input(f"Enter num{i+1}: "))
    x.append(y)
print(max(x))
print(min(x))
#method-2
# for b in range(len(x)):
#     for i in range(len(x)-1):
#         if x[i]>x[i+1]:
#             x[i],x[i+1]=x[i+1],x[i]
#
# print(x[0])
# print(x[-1])
#method-3




