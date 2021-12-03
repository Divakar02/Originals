import random

num1=[i for i in range(5)]
nums=[]
for j in range(5):
    for a in range(5):
        x=float(f'{j}.{a}')
        nums.append(x)
        for b in range(5):
            x = float(f'{j}.{a}{b}')
            nums.append(x)
            for c in range(5):
                x = float(f'{j}.{a}{b}{c}')
                nums.append(x)
                for d in range(5):
                    x = float(f'{j}.{a}{b}{d}')
                    nums.append(x)
                    for e in range(5):
                        x = float(f'{j}.{a}{b}{c}{d}{e}')
                        nums.append(x)
                        for f in range(5):
                            x = float(f'{j}.{a}{b}{c}{d}{e}{f}')
                            nums.append(x)
                            for g in range(5):
                                x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}')
                                nums.append(x)
                                for h in range(5):
                                    x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}')
                                    nums.append(x)
                                    for i in range(5):
                                        x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}')
                                        nums.append(x)
                                        for k in range(5):
                                            x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}')
                                            nums.append(x)
                                            for l in range(5):
                                                x = float(f'{j}.{a}{b}{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}{l}')
                                                nums.append(x)
                                                for m in range(5):
                                                    x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}{l}{m}')
                                                    nums.append(x)
                                                    for n in range(5):
                                                        x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}{l}{m}{n}')
                                                        nums.append(x)
                                                        for o in range(5):
                                                            x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}{l}{m}{n}{o}')
                                                            nums.append(x)
                                                            for p in range(5):
                                                                x = float(f'{j}.{a}{b}{c}{d}{e}{f}{g}{h}{i}{k}{l}{m}{n}{o}{p}')
                                                                nums.append(x)




num2=[i*-1 for i in range(5)]
num=num1+num2+nums

ans=[]
for x in num:
    print(f'Checking {x}')
    if ((2 * x) - 1) * (x + 3) * (x - 2) * ((2 * x) + 3) + 20 == 0:
        ans.append(x)
        ans = list(set(ans))
print(ans)
'''while True:
    for i in num:
        print(f'Checking {i}')
        if ((2*x)-1)*(x+3)*(x-2)*((2*x)+3)+20==0:
            ans.append(x)
            ans=list(set(ans))
    if len(ans)==3:
        ans.sort()
        print(ans)
        break'''
