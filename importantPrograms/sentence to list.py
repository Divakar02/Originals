def sentence_to_list(str):
    str+=" "
    a=''
    list=[]
    for i in str:
        if i!=' ':
            a+=i
        else:
            list.append(a)
            a = ''
    return list

str=input()
print(sentence_to_list(str))


#or

list=str.split(" ")
print(list)

