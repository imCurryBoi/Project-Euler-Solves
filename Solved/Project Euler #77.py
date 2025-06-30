import array

def sieve(num):
    flags = bytearray(num)
    
    flags[2] = 1
    for i in range(3, num, 2):
        flags[i] = 1

    for i in range(3, int(num ** 0.5) + 1, 2):
        if flags[i]:
            for multiple in range(i * i, num, 2 * i):
                flags[multiple] = 0

    return array.array('I', (i for i, flag in enumerate(flags) if flag))

lim = 10**2
parts = sieve(lim)
ways = [1, 0] + [0]*(lim-1) 

for x in parts:
    for i in range(x, lim + 1):
        ways[i] += ways[i-x]

for i in range(0, len(ways)):
    if ways[i] > 5000:
        print(i);break