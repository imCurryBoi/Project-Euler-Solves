from time import time as t

def unit_divide(n): # MAJOR FLAW, DOESNT WORK FOR n DIVISIBLE BY 5
    dividend = 10 ** len(str(n))
    desired_len = len(str(n))
    ans = []
    r = dividend % n
    ans.append(dividend // n)
    c = False
    while True:
        dividend -= ans[-1] * n
        if r == dividend and c:
            if ans[-1] == ans[0]:
                ans = ans[:-1]
                break
            break
        while dividend < n:
            dividend *= 10
        ans.append(dividend // n)
        if dividend % n == 0:  # Termination condition for terminating decimals
            break
        c = True
    return ans

current_max = [0,0]
start = t()

for i in range(11, 10**3, 2):
    if i % 5 != 0:
        x = unit_divide(i)
        if len(x) > current_max[-1]:
            current_max = [i, len(x)]

end = t()
print(current_max, end - start)