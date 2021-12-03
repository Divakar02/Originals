# for i in range(5,0,-1):
#     print(str(i)*(-1*(i-6)))

for i in range(5,0,-1):
    for j in range(-1*(i-6)):
        print(i,end='')
    print()