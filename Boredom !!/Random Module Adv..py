# set1=[1,2,3,4]
# set2=[10,20,30,40]
set1=[1,2,3,True,False]
set2=['a','b','c']
class matrix():
    def choiceany(array):
        convert_to_str=list(map(str,array))
        list_to_set=set(convert_to_str)
        x=list(list_to_set)
        R=x[2]
        if R.isalpha():
            return R
        elif R.isnumeric():
            return int(R)
        elif R in [True,False]:
            return bool(R)
    def choices(*array):
        concod=[]
        for i in array:
            concod.extend(i)
        return matrix.choiceany(concod)





x=matrix.choices(set1)
# y=matrix.choices(set1,set2)
print(x,type(x))