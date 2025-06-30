from itertools import permutations as p
pans = list(p(['1','2','3','4','5','6','7','8','9','0']));c = 0
for pan in pans:
	if int(''.join(pan[3])) % 2 == 0 and int(''.join(pan[5])) % 5== 0 and int(''.join(pan[2:5])) % 3 == 0 and int(''.join(pan[4:7])) % 7 == 0 and int(''.join(pan[5:8])) % 11 == 0 and int(''.join(pan[6:9])) % 13 == 0 and int(''.join(pan[7:])) % 17 == 0:
				c += int(''.join(pan))
print(c)