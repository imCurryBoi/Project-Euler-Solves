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

    return array.array('I', (i for i, flag in enumerate(flags) if flag)).tolist()


def prime_factorize(n, prime_list):
    i = 0
    primes = [[],[]]
    while prime_list[i] ** 2 <= n:
        if n % prime_list[i] != 0:
            i += 1
        else:
            n //= prime_list[i]
            if prime_list[i] in primes[0]:
                primes[1][primes[0].index(prime_list[i])] += 1
                
            else:
                primes[0].append(prime_list[i])
                primes[1].append(1)
                
    if n > 1:
        if n in primes[0]:
            primes[1][primes[0].index(n)] += 1
                
        else:
            primes[0].append(n)
            primes[1].append(1)
    return primes


def factor_sum(n, primes_list):
    ans = 1
    m = 1
    primes = prime_factorize(n, primes_list)

    for i in range(0, len(primes[0])):
        m = (((primes[0][i] ** (primes[1][i] + 1)) - 1) / (primes[0][i] - 1))

        ans *= m

    return ans - n

def is_abundant(n, primes_list):
    if n < 12:
        return False
    return factor_sum(n, primes_list) > n

limit = 28123
prime_list = sieve(int(limit))

abuns = bytearray(limit)

for i in range(0, len(abuns)):
    if abuns[i] != 1:
        if is_abundant(i, prime_list):
            for j in range(i, limit, i):
                abuns[j] = 1
abuns = array.array('I', (i for i, flag in enumerate(abuns) if flag)).tolist()

sums = bytearray(limit)

for i in abuns:
    for j in abuns:
        try:
            sums[i + j] = 1
        except:
            pass

print(sum(array.array('I', (i for i, flag in enumerate(sums) if not flag)).tolist()))