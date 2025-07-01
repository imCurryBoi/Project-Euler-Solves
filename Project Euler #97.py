from time import time as t
'''
def p_l_d(multiplier, base, power, addends, digits):#Prime_last_digits
	digits **= 10
	answer = multiplier
	for i in range(power):
		answer = (answer * base)%digits
	return (answer + addends)%digits
start = t()
print(p_l_d(28433, 2, 7830457, 1, 10), t()- start)'''
#1/11/2025 9:47 am, updated approach, previous takes about 1s
a = t()
print((28433 * pow(2,7830457, 10**10) + 1) % 10**10, t()-a)#takes 0.0s