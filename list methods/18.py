str="pynative@29#8469"
sum=0
count=0
for i in str:
    if i.isnumeric():
        count+=1
        sum+=int(i)

print("Sum =",sum)
print("Average =",sum/count)