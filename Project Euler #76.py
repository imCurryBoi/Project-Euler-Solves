lim = 10**4
parts = [i for i in range(1, lim + 1)]
ways = [1, 0] + [0]*(lim-1) 

for x in parts:
    for i in range(x, lim + 1):
        ways[i] += ways[i-x]

print(ways[-1])