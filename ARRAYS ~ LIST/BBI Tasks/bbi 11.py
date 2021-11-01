bucket=input("Enter the bucket alphabet").split(',')
no_of_words = int(input("Enter the no. of words : "))
d=[]
for i in range(no_of_words):
    d.append(input("Enter the words to form: "))
countValues=[]
for i in range(len(d)):
    count=0
    for j in d[i]:
        if j in bucket:
            count+=1
            bucket.remove(j)
    countValues.append(count)
for i in range(len(countValues)):
    if(len(d[i]))==countValues[i]:
        print('YES')
    else:
        print('NO')
