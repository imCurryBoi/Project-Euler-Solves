def simplify(fraction):
    a1 = fraction[0]; b1 = fraction[1]
    a = a1; b = b1

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return [a1//b, b1//b]

next_convergent = lambda f: simplify([f[0] + 2 * f[1], sum(f)])
convergent = [3, 2]
count = 0

for i in range(1000):
    convergent = next_convergent(convergent)
    if len(str(convergent[0])) > len(str(convergent[1])):
        count += 1

print(count)