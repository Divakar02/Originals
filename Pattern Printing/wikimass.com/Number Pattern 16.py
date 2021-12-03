for i in range(5):
    for j in range(5):
        if j == 0 or (i > 1 and j == 2) or (i > 3 and j == 4):
            print(1,end='')
        if (i != 0 and j == 1) or (i > 2 and j == 3):
            print(0,end='')
    print()