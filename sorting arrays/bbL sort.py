list=[513,135,13,33,22,55,87,312,4]
for i in range(len(list) - 1):
    for j in range(0, len(list)-i-1):
        if list[j] > list[j + 1]:
            list[j], list[j + 1] = list[j + 1], list[j]

print(list)