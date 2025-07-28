from time import time as t
def is_curious(a,b):#Only works for 2 digit numbers
	a_ = str(a)
	b_ = str(b)
	if not(a_[0] == b_[1] or a_[1] == b_[0]):
		return False
	try:
		if a/b == int(a_[0])/int(b_[1]):
			return True
	except:
		pass

	try:
		if a/b == int(a_[1])/int(b_[0]):
			return True
	except:
		pass

	return False

def gcd(a,b):
	if a == b:
		return a
	if a > b:
		return gcd(a-b, b)
	if a < b:
		return gcd(a, b-a)

def simplify(a,b):
	simplifier = gcd(a,b)
	return [a//simplifier, b//simplifier]
start = t()
numerator = 1
denominator = 1
for a in range(10,100):
	for b in range(a + 1, 100):
		if a % 11 != 0:
			if is_curious(a,b):
				numerator *= a
				denominator *= b
print(simplify(numerator, denominator), numerator, denominator, t()-start)
#answer is 1/100 simplified, Jan 26 6:40 pm :)