from time import time

def bouncy_num(n):
    n = list(str(n))

    if len(n) <= 2:
        return False
    
    for i in range(0, len(n)):
        n[i] = int(n[i])
        
    m = n
    asc_n = sorted(n)
    desc_n = sorted(n, reverse = True)

    if (n == asc_n) or (n == desc_n):
        return False
    else:
        return True

percent = 0
i = 1
bouncy = 0

t0 = time()

while percent != 0.99:
    if bouncy_num(i):
        bouncy += 1
    percent = bouncy/i
    i += 1
ans = i - 1

t1 = time()

print(ans)
print(t1 - t0)
