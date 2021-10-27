hangman=['   (_)',
         '  \ | /',
         '    |',
         '   / \\']
hangmancounter=1
word='singaporee'
letters=['_' for i in word]
exceptions=[]
def printer():
    global letters
    print('Country ',end='')
    for i in letters:
        print(i,end=' ')
    print('\n')
printer()
while True:
    letter_input=input("Enter the letter: ")
    while (letter_input in exceptions):
        letter_input=(input("Already given!! Enter anyother letter: ")).lower()
        printer()
    while letter_input.isnumeric() or letter_input.isspace():
        letter_input =input("Invalid!! Enter only alphabets: ")
        printer()
    exceptions.append(letter_input)

    if letter_input in word:
        for i in range(len(word)):
            if letter_input==word[i]:
                letters[i]=letter_input
        printer()
    else:
        print(*hangman[0:hangmancounter],sep='\n')
        print()
        hangmancounter+=1
    if hangmancounter==6:
        print("You lose!!")
        break
    if list(word)==letters:
        print("You win!!")
        break





