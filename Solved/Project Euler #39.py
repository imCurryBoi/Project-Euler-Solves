from time import time
a = time()
ans = [0,0]
for P in range(12, 10**3,2):
	r = 0
	for a in range(1, P):
		if P*(P - 2*a)/(2*(P - a)) == int(P*(P - 2*a)/(2*(P - a))):
			r += 1
	if r > ans[1]:
		ans = [P,r]
print(ans, time() - a)
'''
def is_coprime(a,b):
	while a != b:
		if a > b:
			a -= b
		else:
			b -= a
	if a == 1:
		return True
	return False
def factor(n):
	factors = set()
	for i in range(1, int(n ** 0.5) + 1):
		if n % i == 0:
			factors.add((i, n //i))
	return factors
lim = 10**3
factors = [None] * 10 + [factor(i**2//2) for i in range(10, lim//2,2)]
print(factors)
ways = [0] * (lim + 1)
for i in range(5, len(factors)//2):
	i *= 2
	for j in factors[i]:
		if 2*(j[0] + j[1]) + 3*(i ** 2) < lim:
			ways[2*(j[0] + j[1]) + 3*(i ** 2)] += 1
print(ways.index(max(ways)))'''
