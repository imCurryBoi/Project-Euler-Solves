lim = 10**4;parts = [i + 1 for i in range(lim)];ways = [0]*(lim + 1) + [0];ways[0] = 1 #This is because there is one way to make one
for x in parts:
	if x % 10**3 == 0:
		print(x)
	for i in range(x, lim + 1):
		ways[i] += ways[i-x]
print(ways[lim]%(10**9+7))