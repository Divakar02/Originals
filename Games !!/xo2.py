count=0
L=['①','②','③','④','⑤','⑥','⑦','⑧','⑨']
X=['Ⓧ','Ⓧ','Ⓧ']
O=['Ⓞ','Ⓞ','Ⓞ']
def condi():
    global count
    print('\n', *L[0:3], '\n', *L[3:6], '\n', *L[6:9])
    if L[0:9:2]==X or L[2:7:2]==X or L[0:3]==X or L[3:6]==X or L[6:9]==X or L[0:7:3]==X or L[1:8:3]==X or L[2:9:3]==X:
        print("Player2 is winner!!")
        count=1
    elif L[0:9:2]==O or L[2:7:2]==O or L[0:3]==O or L[3:6]==O or L[6:9]==O or L[0:7:3]==O or L[1:8:3]==O or L[2:9:3]==O:
        print("Player1 is winner!!")
        count=1

print('\n',*L[0:3],'\n',*L[3:6],'\n',*L[6:9])

while True:
    x = int(input("Enter Player1 move(O): ")) - 1
    L[x]='𝕆'
    condi()
    if count==1: break
    y = int(input("Enter Player2 move(X): ")) - 1
    L[y]='𝕏'
    condi()
    if count==1: break





