def even(n):
    return n % 2 == 0

def collatz_sequence_len(n):
    l = 0 # Setting a counter
    while n != 1: # Making a while loop
        if even(n):
            n /= 2
        else:
            n = (3*n + 1)/2
        l += 1
    return l

ans = 0
ans_length = 0

for i in range(3, 10**6, 2):
    l = collatz_sequence_len(i)
    if l > ans_length:
        ans = i
        ans_length = l

print(ans)
print(ans_length)