from itertools import permutations as p

def is_prime(x):
	if (x in [2,3]):
		return True
	elif x %2 == 0:
		return False

	for i in range(3, int(x ** 0.5) + 1, 2):
		if x%i == 0:
			return False
	return True
def gen_pans(n):
	l = list('123456789')[:n]
	return list(p(l))

pans = gen_pans(7)
for i in range(-1, -1 *len(pans), -1):
	if is_prime(int(''.join(pans[i]))):
		print(pans[i])
		break