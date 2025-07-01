''' 5 ms
from time import time as t
from math import comb

start = t()
c = 0
for n in range(1, 101):
    for r in range(1, n):
        if comb(n, r) >= 1000000:
            c +=1
end = t()
print(c, end - start)
''' 
from math import comb
from time import time as t

c = 0
start = t()
for i in range(23, 101):
    for j in range(1, i // 2 + 1):
        if comb(i, j) > 10**6:
            c += i - 2 * j + 1
            break
end = t()
print(c, end - start)#instantaneous