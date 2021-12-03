# with string
for i in range(1,6):
    print(str(i)*i)

# without string
for i in range(1,6):
    for j in range(1,i+1):
        print(i,end='')
    print()