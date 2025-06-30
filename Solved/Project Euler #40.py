def concatenate_Champernowne(d):
    ans = []
    for i in range(1, d + 1):
        for j in range(0, len(str(i))):
            ans.append(int(str(i)[j]))
    return ans

c = concatenate_Champernowne(1000000)
m = c[0] * c[9] * c[99] * c[999] * c[9999] * c[99999] * c[999999]
print(m)

