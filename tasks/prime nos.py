# 2,3,5,7,11,13
#
# for i in range(2,5):
#     for j in range(1,i):
#         if i!=1 and i%j!=0:
#             print(i)
j=2
for i in range(2,10):
    while True:
        x=i%j
        j+=1
        if x==0:
            print(i)
            break
        elif j>i:
            break
