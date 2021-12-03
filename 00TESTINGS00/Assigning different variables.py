count=0
lst=[x for x in range(1,27)]

for i in range(65,91):
    exec(f"{chr(i)}={lst[count]}")
    # exec("%s = %d" % (chr(i),lst[count]))
    count+=1
print(D)