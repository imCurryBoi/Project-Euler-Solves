from time import time as t

def euler_92(n):
    m = str(n)
    while True:
        if n == 89:
            return True
        if n == 1:
            return False
        n = 0
        for i in range(0, len(m)):
            n += int(m[i]) ** 2
        m = str(n)
        
c = 0
t0 = t()

for i in range(1, 10000000):
    if euler_92(i):
        c += 1
    if c%100000 == 0:#To check progress
        print('a')

t1 = t()

print(c)
print(t1 - t0)

