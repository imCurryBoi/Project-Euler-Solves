import array
from time import time as t

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

def prime_factorize(n):
    factors = dict()
    primes_local = primes
    for i in primes_local:
        while n % i == 0:
            n //= i
            if i not in factors:
                factors[i] = 0
            factors[i] += 1
        if n == 1:
            return factors

def count_solutions(factorization):
	c = 1
	for prime in factorization:
		c *= 2*factorization[prime] + 1
	if c % 2 == 0:
		return c // 2
	return (c + 1) // 2

target = 1000
LIM = 5*10**6

primes = sieve(LIM)
start = t()
i = 10

while True:
	if count_solutions(prime_factorize(i)) > target:
		print(i, t() - start)
		break
	i += 1