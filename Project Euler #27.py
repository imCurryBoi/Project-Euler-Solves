import array

def is_prime(n):
    if n == 2 or n == 3:
        return True
    if n <= 1 or n%2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True

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

primes = sieve(1000)
vals = []
Ns = []
for a in range(-999, 1000):
    for b in primes:
        n = 0
        while is_prime(n**2 + a*n + b):
            n += 1
        vals.append([a, b])
        Ns.append(n)
print(max(Ns))
print(vals[Ns.index(max(Ns))])