count=0
# L=['①','②','③','④','⑤','⑥','⑦','⑧','⑨']
L=['_','_','_',
   '_','_','_',
   '_','_','_']
X=['X','X','X']
O=['O','O','O']
exceptions=[]

def condition_for_winning():
    global count
    print('\n', *L[0:3], '\n', *L[3:6], '\n', *L[6:9])

    if L[0:9:2]==O or L[2:7:2]==O or L[0:3]==O or L[3:6]==O or L[6:9]==O or L[0:7:3]==O or L[1:8:3]==O or L[2:9:3]==O:
        print("Player1 is winner!!")
        count=1
    elif L[0:9:2]==X or L[2:7:2]==X or L[0:3]==X or L[3:6]==X or L[6:9]==X or L[0:7:3]==X or L[1:8:3]==X or L[2:9:3]==X:
        print("Player2 is winner!!")
        count=1


print('\n',*L[0:3],'\n',*L[3:6],'\n',*L[6:9])

while True:
    x = int(input("Enter Player1 move(O): "))

    while x in exceptions:
        if x in exceptions:
            x=int(input("Place already Taken!! Try some other move: "))
    exceptions.append(x)

    L[x-1]='O'

    condition_for_winning()
    if '_' not in L:
        print("Draw!!")
        break
    if count==1: break

    y = int(input("Enter Player2 move(X): "))

    while y in exceptions:
        if y in exceptions:
            y = int(input("Place already Taken!! Try some other move: "))
    exceptions.append(y)

    L[y-1]='X'

    condition_for_winning()
    if '_' not in L:
        print("Draw!!")
        break
    if count==1: break







