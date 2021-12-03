lst1=['Name','Class','Sec','Mark']
lst2=['Divakar','12','I','100']
max = max(lst1)
length = len(max)
j = 0
for i in lst1:

    if(length == len(i)):
        print(i+' '*3+lst2[j])
    else:
        space = (length - len(i))+3
        print(i+(' '*space),end='')
        print(lst2[j])
    j+=1
