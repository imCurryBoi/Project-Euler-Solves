def prime_factorize(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return list(set(factors))

def gen_coprimes(n):
    factors = prime_factorize(n)
    flags = bytearray(n)
    flags[1] = 1
    flags[0] = 1

    for i in factors:
        for j in range(i, n, i):
            flags[j] = 1

    return list(array.array('I', (i for i, flag in enumerate(flags) if not flag)))

c = 0
lim = 12000
for i in range(4, lim + 1):
    a = gen_coprimes(i)
    for j in a[:len(a)//2]:
        if 1/3 < j/i:
            c += 1

print(c)