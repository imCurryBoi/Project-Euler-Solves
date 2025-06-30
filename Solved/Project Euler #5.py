#I simply made the smallest possible list of nums
#What's special about that list is that there is a combo of items
#That if you multiply together, you can get any num from 1 - 20.
#So, the list is [2, 2, 2, 2, 3, 3, 5, 7, 11, 13, 17, 19]
# so the answer is the product of the list, 232792560
#Hooray!
from time import time as t
#Later 7/2/2024 11:23 pm
#modified some code from hackerrank projecteuler+ so here u go. A programming repersentation
#doesn't use the primes approach, so def could be optimized
#uses euclids gcd algorithm
'''
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def min_multiple(n):
	x = n
	for i in range(n, 1, -1):
		x *= i//gcd(x,i)
	return x
humanoid = min_multiple(10**6)
with open('Project Euler #5 read/read.txt', 'w') as file:
	file.write(str(humanoid))
#chatgpt - faster
'''
'''
from collections import defaultdict
from math import isqrt

def prime_factors(n):
    """Returns a dictionary of prime factors of n with their highest powers."""
    i = 2
    factors = defaultdict(int)
    # Check for number of 2s that divide n
    while n % i == 0:
        factors[i] += 1
        n //= i
    # n must be odd at this point so a skip of 2 (i = i + 2) can be used
    i = 3
    while i <= isqrt(n):
        # While i divides n, add i and divide n
        while n % i == 0:
            factors[i] += 1
            n //= i
        i += 2
    # This condition is to check if n is a prime number greater than 2
    if n > 2:
        factors[n] += 1
    return factors

def smallest_multiple(n):
    max_factors = defaultdict(int)
    for i in range(2, n + 1):
        factors = prime_factors(i)
        for prime, power in factors.items():
            if power > max_factors[prime]:
                max_factors[prime] = power
    result = 1
    for prime, power in max_factors.items():
        result *= prime ** power
    return result
'''
#my updated one with logarithms and prime sieves 11:08am 7/3/2024
import array
from math import log

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
a = t()
lim = 10**6
primes = sieve(lim)
c = 1
for i in primes:
    c *= i**int(log(lim, i))
b = t()
with open('Project Euler #5 read/read.txt', 'w') as file:
    file.write(str(c))
print(log(c), b-a)