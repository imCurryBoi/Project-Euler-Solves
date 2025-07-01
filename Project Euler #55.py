def is_pal(num):#Checks if palindrome using string splicing
    num = str(num)
    return num == num[::-1]

def lychrel(n):#Uses if/else to check if lychrel
    c = 0
    n += int(str(n)[::-1])

    while True:
        if is_pal(n):
            return False
        elif c == 50:#If #iteration goes above 50, it terminates and returns False
            return True
        else:
            n += int(str(n)[::-1])
            c += 1


c = 0

for i in range(1, 10000):#Self explanatory
    if lychrel(i):
        c += 1
print(c)