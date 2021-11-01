# set1=[1,2,3,4]
# set2=[10,20,30,40]
set1=[True,False]
class matrix():
    def choice(array):
        x= list(map(str, array))
        y=list(map(int,set(x)))
        return y[1]
    def choices(*array):
        concod=[]
        for i in array:
            concod.extend(i)
        return matrix.choice(concod)
    def booleanchoice(array):
        x = list(map(str, array))
        return bool(x[0])

        return array[0]
    def choicestr(array):
        array=list(set(array))
        return array[2]
    def choiceany(array):
        x=list(map(str,set(array)))
        R=x[2]
        if R.isalpha():
            return R
        if R.isnumeric():
            return int(R)
        if R in [True,False]:
            return bool(R)



x=matrix.booleanchoice(set1)
# y=matrix.choices(set1,set2)
print(x,type(x))