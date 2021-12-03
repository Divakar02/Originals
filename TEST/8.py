reg=[[1,35,80],[2,32,75],[3,30,82],[4,33,75],[5,37,60]]

# >35 +2
# <35 -2
final = list(map(lambda x:x[2]+2 if x[1]>35 else x[2]-2,reg))

print(final)