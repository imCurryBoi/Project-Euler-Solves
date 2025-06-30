x = 0
for i in range(1, 2**30 + 1):
    if i ^ (2*i) ^ (3*i)== 0:
        x += 1
print(x)