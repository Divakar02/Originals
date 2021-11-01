alphabet=[chr(i) for i in range(65,91)]
print(alphabet)
dict={}
INPUT=int(input("Select 1 to encode \nSelect 2 to decode \nSelect 0 to quit"))


final=[]

if INPUT==1:
    welcome=list(input("Enter the word to encode: "))
    cipher=list(input("Enter the cipher code: "))
    #Creating the ARRAYS ~ DICTIONARY for cipher:
    for i in range(len(alphabet)):
        dict[alphabet[i]] = cipher[i]
    #Comparing Dict and Cipher:
    for i in range(len(welcome)):
        for key,value in dict.items():
            if key==welcome[i]:
                final.append(value)

print(*final,end='')
