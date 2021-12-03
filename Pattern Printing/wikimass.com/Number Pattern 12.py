# for i in range(1,6):
#     print(str(i)*(-1*(i-6)))

for i in range(1,6):
    for j in range(-1*(i-6)):
        print(i,end='')
    print()