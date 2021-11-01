card=input("Enter the words: ").split(',')
letter_list=input("Enter the letters: ").split(',')
letterinput=''
for i in letter_list:
    letterinput+=i
for word in card:
    if letterinput in word:
        print(word)




