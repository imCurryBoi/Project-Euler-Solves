import array
from time import time as t

def sieve(num):#Sieve for numbers one less than a prime
    flags = bytearray(num)
    
    flags[2 - 1] = 1
    for i in range(3, num, 2):
        flags[i - 1] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i - 1]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple - 1] = 0

    return array.array('I', (i for i, flag in enumerate(flags) if flag))

def this_proj_factor(n):
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            if not is_prime(i + (n//i)):
                return False
    return True

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

    return n+1 in candidates


c = 1 #I notice my answer is 1 off
a = t()
candidates = sieve(10**8)#Takes 9s
print(t()-a)
for i in candidates:
    if i%4 != 0 and i%2 == 0:
        if this_proj_factor(i):
            c += i
print(c, t() - a)