def f(x):
	if x == 2:
		return 2
	return x * f(x - 1)
def binomial(n,k):
	return f(n)/(f(k) * f(n - k))
print(round(7*(1- binomial(60,20)/binomial(70,20)), 9))