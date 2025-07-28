def dot(a,b,c,d):
	return a * c + b * d
def is_right_tri(x1,y1,x2,y2):
	return (dot(x1-x2,y1-y2,x1,y1) == 0 or dot(x1-x2,y1-y2,x2,y2) == 0 or dot(x1,y1,x2,y2) == 0) and (not ((x1, y1) == (0, 0) or (x2, y2) == (0, 0) or (x1, y1) == (x2, y2)))
c = 0	
for i in range(0, 51):
	for j in range(0, 51):
		for k in range(0, 51):
			for l in range(0, 51):
				if is_right_tri(i,j,k,l):
					c += 1
print(c//2)