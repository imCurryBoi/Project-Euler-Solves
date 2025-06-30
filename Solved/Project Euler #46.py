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

def is_prime(n):
	if n % 2 == 0:
		return False
	for i in range(3, int(n ** 0.5 + 1), 2):
		if n % i == 0:
			return False
	return True

lim = 10** 5
squares = [2 * i**2 for i in range(1, lim)]
primes = sieve(lim)
ans = set()
for i in squares:
	for j in primes:
		if i + j > lim:
			break
		ans.add(i + j)
for i in range(3, lim, 2):
	if i not in ans and not is_prime(i):
		print(i)
		break