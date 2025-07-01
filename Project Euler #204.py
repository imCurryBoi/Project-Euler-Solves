import array

def sieve(num):
    num += 1
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return [i for i, flag in enumerate(flags) if flag]

def search(primes, limit, x=1, indexMinPrime=0):
    result = 1

    for i in range(indexMinPrime, len(primes)):
        product = primes[i] * x
        if product > limit:
            break
        result += search(primes, limit, product, i)
    
    return result

def generalisedHammingNumbers(n, k):
    primes = sieve(k)
    return search(primes, n)

if __name__ == "__main__":
    n, k = 10**2, 5
    result = generalisedHammingNumbers(n, k)
    print(result)