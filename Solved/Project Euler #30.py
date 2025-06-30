def fifth_sum(n):
    a = 0
    while n >= 1:
        a += (n % 10) ** 5
        n //= 10
    return a

c = 0
a = 0
for i in range(2, 2*10**5):
    if i == fifth_sum(i):
        c += i
        print(i, c)
print(c)