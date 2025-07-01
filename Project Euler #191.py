from time import time
'''
a = {'a', 'l', 'o'}
vals = {'al' : 1, 'ao' : 1, 'la' : 1, 'lo' : 1, 'oa' : 1, 'ol' : 1, 'oo' : 1}
lim = 2
t = time()
for k in range(lim - 2):
	for i in vals:
		vals[i[-1] + 'o'] += vals[i]
		if i[-1] != 'a':
			vals[i[-1] + 'a'] += vals[i]
		if 'l' not in i:
			vals[i[-1] + 'l'] += vals[i]
print(vals)
print(sum([vals[i] for i in vals]), time()-t)'''
n =10**5

prizes = [[[0 for _ in range(2)] for _ in range(3)] for _ in range(n + 1)]
prizes[0][0][0] = 1#initialization
a = time()
for day in range(1, n + 1):
	for absences in range(3):
		for lates in range(2):
			if prizes[day - 1][absences][lates] > 0:
				prizes[day][0][lates] += prizes[day - 1][absences][lates]
			if absences < 2:
				prizes[day][absences + 1][lates] += prizes[day - 1][absences][lates]
			if lates < 1:
				prizes[day][0][lates + 1] += prizes[day - 1][absences][lates]
c = 0
for absences in range(3):
	for lates in range(2):
		c += prizes[n][absences][lates]
print(c, time() - a)