from math import factorial as f

def f_dig_sum(n):
	n = str(n)
	j = 0
	for i in n:
		j += f(int(i))
	return j

def chain_len(n):
	l = [n]
	m = n

	while True:
		j = f_dig_sum(m)
		m = j
		l.append(m)

		if m in l[0:-1]:
			return len(l) - 1

c = 0

for i in range(1, 10 ** 6):
	if chain_len(i) == 60:
		c += 1
print(c)