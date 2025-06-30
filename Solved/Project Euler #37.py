def Sieve(n):
    prime = [i for i in range(2, n + 1)]
    p = 2
    for i in range(2, int(n ** (1/2)) + 1):
        for j in range(i ** 2, n + 1, i):
            try:
                del prime[prime.index(j)]
            except:
                pass
            
    return prime

print(len(Sieve(100000)))