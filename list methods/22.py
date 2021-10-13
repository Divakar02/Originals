str="Emma25 is data scientist50 and AI expert".split(" ")

for i in str:
    for j in i:
        if j.isnumeric():
            print(i)
            break