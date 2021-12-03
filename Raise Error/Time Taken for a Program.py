import time

start=time.time()

for i in range(100000000):
    x=i

final=time.time()

print(final - start)