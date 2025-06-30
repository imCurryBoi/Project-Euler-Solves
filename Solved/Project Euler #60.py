import array
from math import log
from functools import lru_cache
from time import time as t

log10 = lambda a: log(a, 10)

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


@lru_cache(maxsize=None)
def concatenate(a,b):
    return a * 10**(int(log10(b) + 1)) + b


def is_set_prime(lis):
    for i in range(0, len(lis) - 1):
        for j in range(i + 1, len(lis)):
            if not (is_prime(concatenate(lis[i], lis[j])) and is_prime(concatenate(lis[j], lis[i]))):
                return False
    return True

@lru_cache(maxsize=None)
def is_prime(x):
    x = int(x)
    if x == 2 or x == 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    for i in range(5, int(x**0.5) + 1, 6):
        if x % i == 0 or x % (i+2) == 0:
            return False
    return True

start = t()
lim = 10**4
primes = sieve(lim)

for i in range(0, len(primes)):
    i_ = primes[i]

    for j in range(i + 1, len(primes)):
        j_ = primes[j]
        if is_set_prime([i_, j_]):

            for k in range(j + 1, len(primes)):
                k_ = primes[k]
                if is_set_prime([i_,j_,k_]):

                    for l in range(k + 1, len(primes)):
                        l_ = primes[l]
                        if is_set_prime([i_, j_, k_, l_]):

                            for m in range(l + 1, len(primes)):
                                m_ = primes[m]
                                if is_set_prime([i_, j_, k_, l_, m_]):

                                    print(i_, j_, k_, l_, m_, sum([i_, j_, k_, l_, m_]))
                                    print(t() - start)
                                    quit()
