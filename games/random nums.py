from random import randrange
n=randrange(1000)
while True:
    v=int(input("Enter any num: "))
    if n==v:
        print("You win!")
        break
    print('Smaller try somethin\' bigger' if (n<v) else 'Its Bigger try somethin\' smaller')