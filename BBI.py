bucket=input("Enter the alphabets seperated with comma: ").split(',')
now=int(input("Enter the number of words anne gonna give: "))
# alpha=[]
# for i in range(ran):
#     x=input("Enter the word: ")
# for i in x:
#     alpha.append(i)
# count=1
# # for i in range(len()):
# for i in alpha:
#     if i in bucket:
#         count+=1
#         bucket.remove(i)
#     else:
#         print('no')
#         break
#     if count==len(alpha):
#        print('yes')
count=0
for i in range(now):
    word=input("Enter the words to form")
    for j in word:
        if j in bucket:
            count+=1
            bucket.remove()
    if(len(word)==count):
        print(f"{word}=yes")
    else:
        print(f"{word}=no")










