#This simply calculates the coin probability
from decimal import *
D = lambda a: Decimal(a)
from functools import lru_cache
from time import time as t

getcontext().prec = 20

@lru_cache(maxsize=None)
def factorial(x):
	n = D(1)
	for i in range(1, int(x)):
		n *= D(i)
	return n * x
	
def n_choose_k(n,k):
	return factorial(n)/(factorial(k)*factorial(n-k))

total = D(1000)
target = D(432)
coin = D(0.5)
answer = D(0)
start = t()

for i in range(1, int(target)):
	answer += n_choose_k(total, D(i))

answer = round(1 - answer*(coin ** total), 12)
end = t()
print(answer, end - start)