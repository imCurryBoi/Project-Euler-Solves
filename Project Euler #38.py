from time import time
def is_pan_mul(n):
    a = [str(i*n) for i in range(1, 10)]
    x = ''
    for i in a:
        x = x + i
        if sorted(x) == ['1','2','3','4','5','6','7','8','9']:
            return [True, int(x)]
        if len(x) > 9:
            return [False]

big = 0
a = time()
for i in range(2, 10**5):
    if is_pan_mul(i)[0] and is_pan_mul(i)[1] > big:
        big = is_pan_mul(i)[1]
print(big, time() - a)