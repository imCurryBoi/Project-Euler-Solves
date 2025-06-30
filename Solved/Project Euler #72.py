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


def totient(n):
    factors = prime_factorize(n)
    a = n

    for p in factors:
        a *= (p - 1)/p
    return int(a)


def summatory_totient(n):
    ans = 0
    for i in range(2, n + 1):
        ans += totient(i)
    return ans


print(summatory_totient(10**6))
