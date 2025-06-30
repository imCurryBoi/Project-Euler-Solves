ans = 0
pals = []

def is_pal(num):
    num = str(num)
    willset = False
    for i in range(0, (len(str(num))//2)+1):
        if str(num)[i] == str(num)[((i + 1)*-1)]:
            willset = True
        else:
            willset = False
            break
    if willset:
        return True
    else:
        return False

for i in range(100, 1000):
    for j in range(100, 1000):
        if is_pal(i*j):
            pals.append(i*j)

ans = max(pals)
print(ans)
