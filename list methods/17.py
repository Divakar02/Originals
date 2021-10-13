str=input("Enter the sentence: ").split(" ")
word=input("Enter the word to find: ")
count=0
for i in str:
    if i.lower().startswith(word):
        count+=1

print('Number of words starting with',word,'is',count)

