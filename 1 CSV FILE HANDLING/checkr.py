from functools import reduce

count=0

lst=[303,125,5030]

for num in lst:
    num_list = list(map(int, list(str(num))))

    for i in num_list:
        if i==0:
            num_list.remove(0)
    print(num_list)


    if (num // sum(num_list) == 0) and (num // (reduce(lambda a, b: a * b, num_list)) == 0):
        count += 1

print(count)

