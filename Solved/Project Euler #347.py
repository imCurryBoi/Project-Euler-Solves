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

def find_max(p, q, N):
	max_val = 0
	a = p
	while a <= N:
		b = q
		while b <= N:
			if a * b <= N:
				max_val = max(max_val, a*b)
			else:
				break
			b *= q
		a *= p
	return max_val

def S(N):
    c = 0
    for i in range(len(primes)):
        for j in range(i + 1, len(primes)):
            p = primes[i]
            q = primes[j]
            if p * q > N:
                break
            c += find_max(p, q, N)
    return c

N = 10**7
a = t()
primes = sieve(N//2)

print(S(N), t() - a)
