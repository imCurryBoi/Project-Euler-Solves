import time
from math import floor, sqrt

ans  = 0
limit = 2000000
prime_sum = 0

def is_prime(num):
    if num == 1:
        return False
    
    if num == 2 or num == 3:
        return True

    if num % 2 == 0 and num > 2:
        return False
    
    for i in range(3, floor(sqrt(num)) + 1, 2):
        if num % i == 0:
            return False
    return True

t0 = time.time()

for i in range(1, limit):
    if is_prime(i):
        prime_sum += i

t1 = time.time()

print(prime_sum)
print(t1 - t0)
