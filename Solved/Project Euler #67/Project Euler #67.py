def solve(tri):
	for _ in range(0, len(tri) - 1):
		for i in range(0, len(tri[-2])):
			tri[-2][i] = max(tri[-2][i] + tri[-1][i], tri[-2][i] + tri[-1][i + 1])
		del tri[-1]
	return tri[0][0]

def read_file(f):
	triangle = []
	with open(f , 'r') as file:
		for line in file:
			line = line.split(' ')

			for i in range(0, len(line)):
				line[i] = int(line[i])

			triangle.append(line)
	return triangle

tri = read_file('0067_triangle.txt')
 
print(solve(tri))