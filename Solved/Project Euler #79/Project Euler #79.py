from itertools import permutations as p
def read_file(f):
	attempts = []
	with open(f , 'r') as file:
		for line in file:
			attempts.append(str(int((line))))
	return attempts
file = read_file('file.txt')

a = p(['1', '2', '3', '6', '7', '8', '9', '0'])
for i in a:
	c = 0
	for j in file:
		if i.index(j[0]) < i.index(j[1]) < i.index(j[2]):
			c += 1
	if c == 50:
		print(int(''.join(i)))