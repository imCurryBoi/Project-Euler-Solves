is_cyclical = lambda a, b : a % 100 == int(b / 100)
mini = 10 ** 3;n = 10 ** 4
nums = [
[int((i / 2)*(i + 1)) for i in range(int(0.5 * (-1 + (8 * mini + 1) ** 0.5)) + 1, int(0.5 * (-1 + (8 * n + 1) ** 0.5)) + 1)],
[i**2 for i in range(int(mini ** 0.5 + 1), int(n ** 0.5 + 1))],
[int(0.5*i*(3*i - 1)) for i in range(int((1/6) *(1 + ((24 * mini + 1) ** 0.5))) + 1, int((1/6) *(1 + ((24 * n + 1) ** 0.5))) + 1)],
[i*(2*i - 1) for i in range(int(0.25*(1 + (8 * mini + 1) ** 0.5)) + 1, int(0.25*(1 + (8 * n + 1) ** 0.5)) + 1)],
[int(0.5 * (5 * i - 3) * i) for i in range(int(0.3 + 0.1 * (40 * mini + 9) ** 0.5) + 1, int(0.3 + 0.1 * (40 * n + 9) ** 0.5) + 1)],
[i * (3 * i - 2) for i in range(int((1/3) * (1 + (3 * mini + 1) ** 0.5)) + 1, int((1/3) * (1 + (3 * n + 1) ** 0.5)) + 1)]]
checks = [];checks2 = []
for i in range(0, len(nums)):
        for j in range(0, len(nums)):
                if i != j:
                        for k in nums[i]:
                                for l in nums[j]:
                                        if is_cyclical(k, l):
                                                checks.append([k, i, l, j])
for i in range(4):
        for check in checks:
                for i in range(0, len(nums)):
                        if i not in check:
                                for k in range(0, len(nums[i])):
                                        if is_cyclical(check[-2], nums[i][k]):
                                                checks2.append(check + [nums[i][k], i])
        tupls_list = [tuple(i) for i in checks2]#duplicate_manager and helps to make the cycle run again 
        checks = list(set(tupls_list))          #by taking values from checks2 and putting in check and clearing check2
        checks = [list(i) for i in checks]
        checks2.clear()

# final check
for check in checks:
        if is_cyclical(check[-2], check[0]):
                checks2.append(check)
tupls_list = [tuple(i) for i in checks2]
checks = list(set(tupls_list))
checks = [list(i) for i in checks]
checks2.clear()
print(checks)
print(sum(checks[0][::2]))