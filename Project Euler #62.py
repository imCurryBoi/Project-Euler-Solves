from time import time
def fingerprint(n):#counts digits
	x = 0
	while n > 0:
		x += 10 ** (n % 10)
		n //= 10
	return x

nums = dict()
i = 1
a = time()
while True:
	if fingerprint(i**3) in nums:
		nums[fingerprint(i**3)].append(i)
		if len(nums[fingerprint(i**3)]) >= 5:
			print(min(nums[fingerprint(i**3)]) ** 3, time() - a)
			break
	else:
		nums[fingerprint(i**3)] = [i]
	i += 1