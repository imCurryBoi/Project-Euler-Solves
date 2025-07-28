from math import log
from time import time
a = time()
c = 0
for i in range(1, 10):
    for j in range(1,100):
        if  j - 1 <= j*log(i, 10) < j:
            c += 1
print(c, time() - a)