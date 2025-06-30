from time import time as t
def sieve(num):
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return [i for i, flag in enumerate(flags) if flag]

a = t()
lim = 10**8
primes = sieve(lim//2)
print(t() - a)
pi_s = [0] * lim
for i in range(0, len(primes)):
    pi_s[primes[i]] = i + 1
for i in range(0, len(pi_s)):
    if pi_s[i] == 0:
        pi_s[i] = pi_s[i - 1]
print(t() - a)

c = 0
for i in primes:
    x = lim//i
    c += pi_s[x]
print(t() - a)
print(c)
