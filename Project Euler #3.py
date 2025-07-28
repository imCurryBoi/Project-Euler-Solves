from random import randint as ran
from time import time as t
def largest_factor(n):
    lim = int(n)
    a = 0
    while n % 2 == 0:
        n //= 2
        a = 2
    factor = 3
    while factor ** 2 <= lim:
        if n % factor == 0:
            n //= factor
            a = factor
        else:
            factor += 2
    if n > a:
        return n
    return a
def is_prime(x):
    if x % 2 == 0:
        return False
    i = 5
    while i ** 2 <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True
a = t()
for i in range(10):
    x = ran(10 ** 11, 10 ** 15)
    y = largest_factor(x)
    z = is_prime(y)
    print(x, y, z)
print(t() - a)
