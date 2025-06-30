ans = 2
num = 1
fib_num = 1
fib_num2 = 0

while len(str(num)) < 1000:
    fib_num2 = num
    num += fib_num
    fib_num = fib_num2
    ans +=1

print(ans)
