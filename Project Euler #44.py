def is_pent(p):
	return (((24*p + 1) ** (1/2)) + 1) / 6 == (((24*p + 1) ** (1/2)) + 1) // 6
def pent(n):
	return n * ((3 * n) - 1) // 2

x = True
e = 2

while x:
	for i in range(1, e):
		if is_pent(pent(i) + pent(e)) and is_pent(pent(e) - pent(i)):
			print(pent(e) - pent(i))
			x = False
	e += 1