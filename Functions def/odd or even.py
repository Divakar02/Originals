# list1[0],list2[i]=list2[i],list1[0]
list1=[2,4,6,1]
list2=[1,3,5,2]

condition=sum(list1)%2==0 and sum(list2)%2==0

def odd_even(list):
    even=0
    odd=0
    for i in list:
        if i%2==0:
            even+=1
        else:
            odd+=1
    return f'odd={odd}\neven={even}'

print(odd_even(list1))

