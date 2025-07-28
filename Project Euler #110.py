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

def prod(lis, i = 0, current = 1):
    if i == len(lis):
        return current
    return prod(lis, i + 1, current * lis[i])


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
#all right so the way this works is using the factor counting formula
#using prime factors, simple problem #108 logic
target = 4*10**6
start = t()

primes = sieve(10**4)#The necessary number for this is dependent on how high i gets in the final loop

i = 0
multiplier = [1]

while count_solutions(prime_factorize(prod(multiplier))) < target:
    multiplier.append(primes[i])
    i += 1
#using a forum post from the original #108, i figured that the answer is always a multiple of a group of consecutive primes
multiplier = prod(multiplier[:-3])#the index is like a filter, the more it is the more chance your answer is correct
#because the less consecutive primes, the smaller the multiple and therefore more possibilities are checked
#3 works for problem #110, while purely 1 works for #108

i = 1
#This loops just checks multiples
while True:
    temporary = multiplier * i
    temp_solutions = count_solutions(prime_factorize(temporary))
    if temp_solutions > target:
        end = t()
        print(temporary, temp_solutions, i,end - start)
        break
    i += 1

#1/22/2025 8:37 pm