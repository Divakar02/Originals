lst = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
values = []
turn = 0
print("     TIC TAC TOE GAME \n")
while 1:
    for i in lst:
        print(i)
    if (lst[0][0] == lst[1][1] == lst[2][2]):
        ans = lst[0][0]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[0][2] == lst[1][1] == lst[2][0]):
        ans = lst[0][2]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[0][0] == lst[0][1] == lst[0][2]):
        ans = lst[0][0]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[1][0] == lst[1][1] == lst[1][2]):
        ans = lst[1][0]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[2][0] == lst[2][1] == lst[2][2]):
        ans = lst[2][0]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[0][0] == lst[1][1] == lst[2][2]):
        ans = lst[0][0]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[0][1] == lst[1][1] == lst[2][1]):
        ans = lst[0][1]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break

    elif (lst[0][2] == lst[1][2] == lst[2][2]):
        ans = lst[0][2]
        if ans == "o":
            print("\n\nPlayer-1 Won")
        else:
            print("\n\nPlayer-2 Won")
        break
    elif len(values) == 9:
        print("\n Game Draw ")
        break

    else:
        None

    if turn % 2 == 0:
        o = int(input("Player-1(Enter the position):"))

        if o in values:
            print("\nThis position is already used!!!!\n")
            turn -= 1
        else:
            values.append(o)
            if o <= 3:
                lst[0][lst[0].index(o)] = "o"
            elif (o > 3) and (o <= 6):
                lst[1][lst[1].index(o)] = "o"
            else:
                lst[2][lst[2].index(o)] = "o"


    else:
        x = int(input("Player-2(Enter the position):"))

        if x in values:
            print("\nThis position is already used!!!\n")
            turn -= 1
        else:
            values.append(x)
            if x <= 3:
                lst[0][lst[0].index(x)] = "x"
            elif (x > 3) and (x <= 6):
                lst[1][lst[1].index(x)] = "x"
            else:
                lst[2][lst[2].index(x)] = "x"

    turn += 1