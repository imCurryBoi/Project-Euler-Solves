nums = []
ans = 0
for i in range(1,1000):
    if i%3 == 0:
        nums.append(i)
    elif i%5 == 0:
        nums.append(i)

for i in range(0, len(nums)):
    ans += nums[i]

print(ans)
