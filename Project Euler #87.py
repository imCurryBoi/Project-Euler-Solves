import array

def sieve(num):
    if num == 2:
        return [2]
    if num == 3:
        return [2, 3]
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return list(array.array('I', (i for i, flag in enumerate(flags) if flag)))
lim = 5 * 10**7
d = [i ** 2 for i in sieve(int(lim ** (1/2)))]
t = [i ** 3 for i in sieve(int(lim ** (1/3)))]
f = [i ** 4 for i in sieve(int(lim ** (1/4)))]
c = set()

for i in d:
    for j in t:
        if lim < i + j:
            break
        for k in f:
            if i + j + k < lim:
                c.add(i + j + k)
            else:
                break
print(len(c))