lst=[3,2,11,7,6,5,6,1]
# lst2=[2,1,7,6,5,1,1,-1]
lst2=[]

# for i in range(len(lst)):
#     for j in range(len(lst)-2):
#         srt=sorted(lst[i+1::])
#         print(srt)
#         if srt[j]<lst[i]:
#             lst2.append(srt[j])
#             break

for i in range(len(lst)):
    x=lst[i+1::]
    for j in sorted(x):
        if x[i]<j:
            lst2.append(j)



print(lst2)

