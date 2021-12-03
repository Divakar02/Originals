second=3600


# 1,12,30,12,59,59
lst=[0,0,0,0,0,0]
# 1year=31104000
# 1month=2592000
# 1day=86400
# 1hour=3600
# 1minute=60
def convert(seconds):
    seconds %= (12*30 * 24 * 3600)
    year = seconds // 12
    seconds %= (30*24*3600)
    months = seconds // 30
    seconds %= (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60

    return "{seconds}:{year}:{}{hour}:{minutes}:{seconds}"


# Driver program
n = 1801
print(convert(n))



