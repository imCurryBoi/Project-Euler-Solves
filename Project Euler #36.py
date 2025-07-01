def is_pal_both(num):
    b = bin(num)[2:]
    num = str(num)
    
    for i in range(0, (len(num) // 2) + 1):
        if str(num)[i] == str(num)[((i + 1)*-1)]:
            pass

        else:
            return False

    for i in range(0, (len(b) // 2) + 1):
        if str(b)[i] == str(b)[(i + 1) * -1]:
            pass

        else:
            return False
    return True

c = 0

for i in range(1, 1000000):
    if is_pal_both(i):
        c += i
        print(i)
        
print(c)

