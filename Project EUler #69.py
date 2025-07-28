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

def totient_max_ratio(limit):
    primes = sieve(int(limit ** 0.33))#The cbrt works for large limits
    ans = 1; i = 0
    while ans < limit/primes[i]:
        ans *= primes[i]
        i += 1
        
    return ans

print(totient_max_ratio(10**6))
print(len(sieve(1.5*10**5))**5)