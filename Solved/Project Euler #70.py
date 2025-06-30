import array

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

lim = 10**7
primes = sieve(int(lim))

def is_perm(a, b):
    return sorted(list(str(int(a)))) == sorted(list(str(int(b))))


n_s = []
phi_s = []

for i in primes:
    for j in primes:
        if i * j < 
        if i * j < 10**7 and is_perm(i * j, (i - 1) * (j - 1)):
            n_s.append(i * j)
            phi_s.append((i * j) / ((i - 1) * (j - 1)))
        else:
            break

print(min(phi_s), n_s[phi_s.index(min(phi_s))])