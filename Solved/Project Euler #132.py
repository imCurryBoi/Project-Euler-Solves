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

primes = sieve(10**7)

def does_div_repunit(repunit_length, divisor):
    return pow(10, repunit_length, 9*divisor) == 1

divisors = []
repunit_length = 10 ** 9
required_factors = 40

for prime in primes:
    if does_div_repunit(repunit_length, prime):
        divisors.append(prime)
        if len(divisors) == 40:
            break

print(divisors, sum(divisors), len(divisors))