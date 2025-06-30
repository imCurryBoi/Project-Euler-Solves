import array
from time import time as t
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

def binomial_gen(total_rows):
    rows = [[1], [1, 1]]
    while len(rows) < total_rows:
        current = [1] + [0] * (len(rows) - 1) + [1]
        for i in range(1, len(current) - 1):
            current[i] = rows[-1][i] + rows[-1][i - 1]
        rows.append(current)
    a = set()
    for i in rows:
        for j in i:
            a.add(j)
    return a
def is_square_free(n):
    local_squares = squares
    for i in local_squares:
        if n % i == 0:
            return False
    return True
lim = 51
a = t()
nums = binomial_gen(lim)
m = max(nums)
c = sum(nums)
primes = list(sieve(lim ** 0.5))
squares = [i ** 2 for i in primes]
c = 0

for i in nums:
    if is_square_free(i):
        c += i
print(c, t()-a)