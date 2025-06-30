gpGen = lambda a: a * (3 * a - 1) // 2
parts = [1]  # Partitions (p(0) = 1)
c = 1# Counter for current number to partition
p = 10**9+7
d = None
while True:
    d = 0
    k = 1
    while True:
        g_k1 = gpGen(k)
        g_k2 = gpGen(-k)

        if g_k1 > c:
            break

        d += parts[c - g_k1] * ((-1) ** (k - 1))
        d %= p
        if g_k2 <= c:
            d += parts[c - g_k2] * ((-1) ** (k - 1))
            d %= p

        k += 1

    parts.append(d)
    c += 1
    if len(parts) == 6*10**4 + 1:
        break

print(c - 1)
print(parts[-1])