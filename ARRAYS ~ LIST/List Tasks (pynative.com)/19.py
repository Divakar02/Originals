str = "Emma is a data scientist who knows python. Emma works in google."
strlist = str.split(" ")
list=[]
for i in range(len(str)):
    if str[i].lower()=='e':
        if str[i:i+4].lower()=='emma':
            list.append(i)

print("The index of final word that starts with emma is",max(list))


