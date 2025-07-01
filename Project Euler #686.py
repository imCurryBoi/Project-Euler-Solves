from math import log10
from time import time as t

def first_3_powers_of_2(power):
	log_fractional_part = power*log10(2) % 1
	return int(10**log_fractional_part*100)

i = 12710
current_n = 45
start = t()

while current_n != 678910:
	if first_3_powers_of_2(i) == 123:
		current_n += 1
	i += 1

end = t()

print(i-1, end - start) #34.32 s
