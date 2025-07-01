ans = 0
factor = 1
reps = int(input("How many reps? "))

for i in range(1, reps + 1):
    factor *= i

factor = str(factor)

for i in range(0, len(factor)):
    ans += int(factor[i])

print(ans)
