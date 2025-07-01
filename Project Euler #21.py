def sum_factor(n):
	s = 1
	for i in range(2, int(n**0.5) + 1):
		if n % i == 0:
			s += i
			if n/i != i:
				s += n//i
	return s

def amicable(n):
	s1 = sum_factor(n)
	if s1 != n:
		return sum_factor(s1) == n
	return False

amicable_sum = 0

for i in range(1, 10**4):
	if amicable(i):
		amicable_sum += i

print(amicable_sum)