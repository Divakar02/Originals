d= [{'country':'india','sale':150.2},
{'country':'china','sale':250.2},
{'country':'malasia','sale':149},
{'country':'America','sale':130.9}]


y=list(filter(lambda d:d[1],d))

print(y)