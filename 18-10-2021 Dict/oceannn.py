word=input("Enter the word: ")
for i in range(len(word)):
    for j in range(len(word)):
        if (i==j):
            print(word[i],end=' ')
        if i+j==len(word)-1 and i!=2:
            print(word[-(i+1)], end=' ')

        else:
            print(' ',end=' ')
    print()