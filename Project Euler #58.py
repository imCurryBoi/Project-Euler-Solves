import random
from time import time as t
def is_prime(x):
	if x % 2 == 0 or x % 3 == 0:
		return False
	for i in range(5, int(x ** 0.5) + 1, 6):
		if x % i == 0 or x % (i + 2) == 0:
			return False
	return True

def miller_rabin(n, k=3):
    # If n is less than 2, it's not prime
    if n <= 1:
        return False
    # 2 and 3 are prime numbers
    if n <= 3:
        return True
    # Exclude even numbers
    if n % 2 == 0:
        return False
    
    # Write n as d * 2^r + 1 with d odd (by factoring out powers of 2 from n-1)
    r, d = 0, n - 1
    while d % 2 == 0:
        r += 1
        d //= 2
    
    # Test k times
    for _ in range(k):
        # Pick a random integer a in the range [2, n − 2]
        a = random.randint(2, n - 2)
        # Compute a^d % n
        x = pow(a, d, n)
        
        if x == 1 or x == n - 1:
            continue
        
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    
    return True

length = 2
primes = 3
i = 9
start = t()
while primes/(4*length-3) > 0.1:
	for _ in range(4):
		i += 2 * length
		if miller_rabin(i):
			primes += 1
	length += 1
end = t()
print(2*length-1, end - start)