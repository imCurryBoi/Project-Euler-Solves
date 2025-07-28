from time import time as t

def is_shortest_route_integer(a, b, c):
    return (((a+b) ** 2 + c ** 2) ** 0.5) % 1 == 0

c = 0
solutions = 0
limit = 10**6
start = t()

while solutions <= limit:
    c += 1
    for b in range(1, c + 1):
        for a in range(1, b + 1):
            if is_shortest_route_integer(a,b,c):
                solutions += 1

end = t()

print(c)
print(solutions)
print(end - start)