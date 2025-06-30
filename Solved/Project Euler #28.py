answer = 1
primes = 8
counter = 49
i = 8
'''
for	i in range(2, limit, 2):
	for j in range(4):
		counter += i
		answer += counter

print(answer)
'''

def is_prime(num):
    if num % 2 == 0:
        return False
    for i in range(3, int(num ** 0.5), 2):
        if num % i == 0:
            return False
    return True

while True:
	i += 2
	for j in range(4):
		counter += i
		if is_prime(counter):
			primes += 1
		if primes / (int(counter ** 0.5) * 2 - 1) <= 0.1:
			print((int(counter ** 0.5) * 2 - 1))
			break
