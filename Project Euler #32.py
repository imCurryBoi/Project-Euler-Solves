from time import time as t

def prod_pan(n1, n2):
    prod = list(str(n1 * n2))
    n1 = list(str(n1))
    n2 = list(str(n2))
    z = sorted(prod + n1 + n2)
    num_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

    if z == num_list:
        return True
    else:
        return False

c = []
t0 = t()

for i in range(1, 100):
    for j in range(100, 10000):
        if prod_pan(i, j):
            if (i * j) not in c:
                c.append(i * j)

ans = sum(c)
t1 = t()

print(ans)
print(t1 - t0)
