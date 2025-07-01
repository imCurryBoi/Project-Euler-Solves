from time import time as t

x = 0
start = t()

for i in range(1, 2**30 + 1):
    if i ^ (2*i) ^ (3*i)== 0:
        x += 1
end = t()
print(x, end-start) #103.2 s