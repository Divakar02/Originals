import time

title=['Year','Month','Date','Hour','Min','Sec','WDay','Yday','Isdst']
dict={title[i]:time.gmtime()[i] for i in range(8)}
# print(dict)
for i,j in dict.items():
    print(i,'     ',j)
