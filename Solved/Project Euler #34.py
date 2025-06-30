from time import time as t
from math import factorial as ft

def ft_dig_sum_num(num):
    c = 0
    n = num
    num = list(str(num))

    for i in range(0, len(num)):
        num[i] = int(num[i])
        c += ft(num[i])

    if c == n:
        return True
    else:
        return False

c = 0
t0 = t()

for i in range(10, 3265920):
    if ft_dig_sum_num(i):
        c += i

t1 = t()

print(c)
print(t1 - t0)
