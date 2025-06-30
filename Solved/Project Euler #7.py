j = 3
primes = [2, 3]
def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(2, num//2 + 1):
        if num % i == 0:
            return False
    return True

while len(primes) <= 10003:
    j += 1
    if is_prime(j):
        primes.append(j)

print(primes[10000])
