def this_project_read_lines(f):
	with open(f , 'r') as file:
		for line in file:
			line = line.split('","')
			return sorted(line)
def score(name, pos):
	name = name.upper()#This makes the name all uppercase

	A = name.count('A')
	B = name.count('B')
	C = name.count('C')
	D = name.count('D')
	E = name.count('E')
	F = name.count('F')
	G = name.count('G')
	H = name.count('H')
	I = name.count('I')
	J = name.count('J')
	K = name.count('K')
	L = name.count('L')
	M = name.count('M')
	N = name.count('N')
	O = name.count('O')
	P = name.count('P')
	Q = name.count('Q')
	R = name.count('R')
	S = name.count('S')
	T = name.count('T')
	U = name.count('U')
	V = name.count('V')
	W = name.count('W')
	X = name.count('X')
	Y = name.count('Y')
	Z = name.count('Z')
	#This counts the number of each letter in the user's name

	return ((A+B*2+C*3+D*4+E*5+F*6+G*7+H*8+I*9+J*10+K*11+L*12+M*13+N*14+O*15+P*16+Q*17+R*18+S*19+T*20+U*21+V*22+W*23+X*24+Y*25+Z*26)*pos)#This finds out the lucky using this formula

file = this_project_read_lines('file.txt')
ans = 0

for i in range(0, len(file)):
	ans += score(file[i], i + 1)

print(ans)
