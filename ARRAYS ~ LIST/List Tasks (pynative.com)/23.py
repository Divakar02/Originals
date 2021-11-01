str="Welcome to usa.uas USA is awesome isn't it?"
strf=''
count=0
for i in range(len(str)):
    if str[i]=='u' or str[i]=='U':
        if str[i+1]=='s' or str[i+1]=='S':
            if str[i+2] == 'a' or str[i+2] == 'A':
                count+=1

print(count)

