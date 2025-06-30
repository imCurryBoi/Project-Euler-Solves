ans = 0
reps = int(input("How many repititions? "))
sum_square = (((reps+1)*(reps))//2)**2
square_sum = 0

for i in range(1, reps + 1):
    square_sum += i**2

ans = sum_square - square_sum
print(ans)
