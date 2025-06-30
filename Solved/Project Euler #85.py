	def abs(x):
		return int((x ** 2) ** 0.5)
	def count(a,b):
		return int((a**2 + a)*(b**2+b)/4)
	current_area = 0
	current_count = 0
	lim = 2*10**6
	for x in range(2, 101):
		for y in range(2, x):
			if abs(count(x,y) - lim) < abs(lim - current_count):
				current_count = count(x,y)
				current_area = x * y
	print(current_count, current_area)