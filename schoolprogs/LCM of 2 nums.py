x,y=int(input('Enter num1: ')),int(input('Enter num2: '))

max=max(x,y)

while True:
    if max%x==max%y==0:
        print('LCM =',max)
        break
    else:
        max+=1