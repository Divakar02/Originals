count=0
L=['_','_','_',
   '_','_','_',
   '_','_','_']

def condi():
    global count
    if L[0]==L[4]==L[8]=='X' or L[2]==L[4]==L[6]=='X' or L[0]==L[1]==L[2]=='X' or L[3]==L[4]==L[5]=='X' or L[6]==L[7]==L[8]=='X' or L[0]==L[3]==L[6]=='X' or L[1]==L[4]==L[7]=='X' or L[2]==L[5]==L[8]=='X':
        print("Player2 is winner!!")
        count += 1
    elif L[0]==L[4]==L[8]=='O' or L[2]==L[4]==L[6]=='O' or L[0]==L[1]==L[2]=='O' or L[3]==L[4]==L[5]=='O' or L[6]==L[7]==L[8]=='O' or L[0]==L[3]==L[6]=='O' or L[1]==L[4]==L[7]=='O' or L[2]==L[5]==L[8]=='O':
        print("Player1 is winner!!")
        count += 1

print('\n',L[0], L[1], L[2],'\n',L[3], L[4], L[5],'\n',L[6], L[7], L[8])

while True:
    x = int(input("Enter Player1 move(O): "))
    L[x-1]='O'
    print('\n', L[0], L[1], L[2], '\n', L[3], L[4], L[5], '\n', L[6], L[7], L[8])
    condi()
    if count==1: break
    y = int(input("Enter Player2 move(X): "))
    L[y-1]='X'
    print('\n', L[0], L[1], L[2], '\n', L[3], L[4], L[5], '\n', L[6], L[7], L[8])
    condi()
    if count==1: break





