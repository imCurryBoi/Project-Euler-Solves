terms = set()
lim = 10**2
for a in range(2, lim + 1):
    for b in range(2, lim + 1):
        terms.add(a**b)
print(len(terms))
