ans = 0

def digits_odd(num):#Checks if all the digits of a # are odd
    num = str(num)

    for i in range(0, len(num)):
        if int(num[i])%2 != 1:
            return False

    return True

def rev_add(n):#Adds # to its reverse
    return n + int(str(n)[::-1])

        
for i in range(1, 10**8,2):
    if i % 10 != 0:
        if digits_odd(rev_add(i)):
            ans += 1
print(ans)