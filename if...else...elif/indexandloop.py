sent=str(input("Enter the sentence : "))
letter=str(input("Enter the letters that begins with: "))
listA=sent.split()
print(listA)

final=[i for i in listA if i[0]==letter]
print(final)