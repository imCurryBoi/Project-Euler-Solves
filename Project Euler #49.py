import array
from itertools import combinations as c
def combos(a):
    return list(c(a,3))

def sieve(floor, num):
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    r = array.array('I', (i for i, flag in enumerate(flags) if flag)).tolist()
    for i in range(0, len(r)):
        if r[i] > floor:
            return r[i:]


primeOG = sieve(10**3 + 1, 10 ** 4 - 1)
d = {}
primes = sieve(10**3 + 1, 10 ** 4 - 1)

for i in range(0, len(primes)):
    primes[i] = sorted(list(str(primes[i])))

for i in range(0, len(primes)):
    if primes.count(primes[i]) >= 3:
        if ''.join(primes[i]) in d:
            d[''.join(primes[i])].append(primeOG[i])

        else:
            d[''.join(primes[i])] = [primeOG[i]]

keylist = d.keys()

for i in keylist:
    hi = combos(d[i])
    for j in hi:
        if j[1] - j[0] == j[2] - j[1]:
            print(d[i]) 