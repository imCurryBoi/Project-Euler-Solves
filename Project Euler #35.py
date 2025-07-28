def cycle(n):#For integers
    m = str(n)
    a = []
    for i in range(len(m)):
        k = ''
        for j in range(len(m)):
            k = k + m[(i + j) % len(m)]
        a.append(int(k))
    return a

def is_prime(n):
    for i in range(2, int(n ** (1/2)) + 1):
        if n % i == 0:
            return False

    return True
def digits_odd(num):#Checks if all the digits of a # are odd
    num = str(num)

    for i in range(0, len(num)):
        if int(num[i])%2 != 1:
            return False

    return True

def is_circular_prime(n):
    if n == 2:
        return True

    if (not is_prime(n)) or (not digits_odd(n)):
        return False
    else:
        for num in cycle(n):
            if not is_prime(num):
                return False
    return True

c = 0

for i in range(2, 10**6):
    if is_circular_prime(i):
        c += 1

print(c)