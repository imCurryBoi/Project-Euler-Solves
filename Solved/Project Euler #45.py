from time import time as t

def is_pent(p):
    return ((((24 * p + 1) ** (1 / 2)) + 1)) / 6 == ((((24 * p + 1) ** (1 / 2)) + 1)) // 6

def hexa(x):
     return x * (2 * x - 1)

c = 144
t0 = t()

while not is_pent(hexa(c)):
    c += 1

t1 = t()

print(hexa(c))
print(t1 - t0)
