import time

title=['Year','Month','Date','Hour','Min','Sec','WDay','Yday','Isdst']
data=[data for data in time.gmtime()]


def order(title,data):
    for i in range(len(title)):
        string = ' ' * ((len(max(title))+1) - len(title[i]))
        print(title[i],string,data[i])

order(title,data)

