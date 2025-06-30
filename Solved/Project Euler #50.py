import array
from time import time
def sieve(num):
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return array.array('I', (i for i, flag in enumerate(flags) if flag))

lim = 10**6
current = 0
primes = sieve(lim)
ans = set()

a = time()
for i in range(0, len(primes)):
    if primes[i] > lim * 0.0001:#from tests
        break
    for j in range(i + 1, len(primes)):
        if sum(primes[i:j]) in primes:
            current = (sum(primes[i:j]), j - i, primes[i])
        if sum(primes[i:j]) > lim:
            break
    ans.add(current)

current = (0, 0)
for i in ans:
    if i[1] > current[1]:
        current = i
b = time()
print(current)
print(b-a)