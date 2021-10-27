list = list(map(int, input("Enter comma separated values: ").split(",")))
print('Given Numbers    =>',list)
# greater swap
for b in range(len(list)):
    for i in range(len(list)-1):
        if list[i]>list[i+1]:
            list[i],list[i+1]=list[i+1],list[i]

print('Ascending Order  =>',list)
print('Descending Order =>',list[::-1])
