num1 = [i for i in range(5)]
nums = []
N = int(input("Range of Numbers.........?"))
D = int(input("How many decimal places..?"))

for j in range(N):
    if D >= 1:
        for a in range(100):
            x = float(f'{j}.{a}')
            nums.append(x)
        if D >= 2:
            for b in range(100):
                x = float(f'{j}.{a}{b}')
                nums.append(x)
            if D >= 3:
                for c in range(100):
                    x = float(f'{j}.{a}{b}{c}')
                    nums.append(x)
                if D >= 4:
                    for d in range(100):
                        x = float(f'{j}.{a}{b}{d}')
                        nums.append(x)
                    if D >= 5:
                        for e in range(100):
                            x = float(f'{j}.{a}{b}{c}{d}{e}')
                            nums.append(x)
                        '''for f in range(5):
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
f                                                        nums.append(x)'''
import time

try:
    time.sleep(10)
    try:
        time.sleep(10)
        try:
            time.sleep(10)
            for i in nums:
                print(i)
                time.sleep(0.2)
        except KeyboardInterrupt:
            exec(f'{input("Enter any:")}')
    except KeyboardInterrupt:
        exec(f'{input("Enter any:")}')
except KeyboardInterrupt:
    exec(f'{input("Enter any:")}')



