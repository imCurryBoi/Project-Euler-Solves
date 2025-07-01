def modular_tetrate(base, power, mod):
    ans = base
    for _ in range(power - 1):
        ans = pow(base, ans, mod)
    return ans
print(modular_tetrate(1777,1855, 10**8))