from math import log10, sqrt
from decimal import Decimal as dec
from time import time as t

def is_pan(n):
    return sorted(str(n)) == list('123456789')
def fibbonaci_first_9(n):
    phi = dec(1.61803398874989484820458683436563811772030917980576286213544862270526046281890)
    fractional_part = (n * log10(phi) - log10(sqrt(5))) % 1#The first part is approximately log(fib(n))
    first_9 = int(10**fractional_part * 10**8)
    return first_9

start = t()
nums = [1,1]
k = 2
mod = 10**9
while True:
    nums.append((nums[-1] + nums[-2]) % 10**9)
    k += 1
    del nums[0]
    if is_pan(nums[-1]):
        if is_pan(fibbonaci_first_9(k)):
            print(k)
            break
end = t()
print(end - start)