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

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def fingerprint(n):#counts digits
	x = 0
	while n > 0:
		x += 10 ** (n % 10)
		n //= 10
	return x