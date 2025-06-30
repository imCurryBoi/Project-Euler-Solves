from time import time as t
import array
def sieve(num):
    num = int(num + 1)
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return array.array('I', (i for i, flag in enumerate(flags) if flag))
def num_of_factors(num):
    c = 1
    for i in primes:
        c2 = 0
        while num % i == 0:
            num //= i
            c2 += 1
        if c2 > 0:
            c *= c2 + 1
        if num == 1:
            return c
    return c
a = t()
req = 1000
primes = sieve(842161320 ** 0.5)#the 1000 divisor tri number
n = 1
dic = {-3:-4}
while True:
    q = 0
    tri = n * (n + 1) // 2
    x = num_of_factors(tri)
    for i in dic:
        if i > req:
            q += 1
    if q > 0:
        break 

    if x > max(dic):
        dic[x] = tri
    n += 1
print(dic[max(dic)])
print(t() - a)