import random

hangman = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']
hangmancounter=1
dict={
'country':['India','Pakistan','America','England',],
'movies':['Spy Kids','Inception','Titanic','Avengers','Justice League'],
'sports':['cricket','hockey','tennis','chess','carrom','kabadi']
}

# mix=random.choice(mix)
user_word=input("Welcome to the Games !! :)\n\nEnter the choice of yours:\n Country\n Movies\n Sports\n Mix\n")
while user_word.lower() not in dict.keys():
    user_word=input("Please enter valid word: ")
word='justice league'
# word=random.choice(dict[user_word.lower()]).lower()
print(word)
letters=[]
for i in word:
    if not i.isspace():
        letters.append('_')
    else:
        letters.append(' ')

exceptions=[]

def printer():
    global letters
    print(*hangman[0:hangmancounter], sep='\n')
    print(f'Guess the {user_word} ',end='\n')
    for i in letters:
        print(i,end=' ')
    print('\n')
printer()
while True:
    printer()
    letter_input=input("Enter the letter: ")
    while (letter_input in exceptions):
        letter_input=(input("Already given!! Enter any other letter: ")).lower()
    while letter_input.isnumeric() or letter_input.isspace():
        letter_input =input("Invalid!! Enter only alphabets: ")
    exceptions.append(letter_input)

    if letter_input in word:
        for i in range(len(word)):
            if letter_input==word[i]:
                letters[i]=letter_input
    else:
        print()
        hangmancounter+=1

    if hangmancounter==8:
        reader=open('C:/Users/Divakar/Desktop/Hangman.txt','w')
        print(reader)
        print("You lose!!")
        break

    if list(word)==letters:
        print("You win!!")
        break





