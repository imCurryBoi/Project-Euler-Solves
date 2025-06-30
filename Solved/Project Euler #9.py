from time import time as t
a = t()
ans = 0
for P in range(10**3,10**3 + 1):
	r = 0
	for a in range(1, P):
		b = P*(P - 2*a)/(2*(P - a))
		if b == int(b):
			if a * b * (P - a - b) > ans:
				ans =  a * b * (P - a - b)
print(ans, t() - a)