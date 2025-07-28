def reduce(fraction):
    a1 = fraction[0]; b1 = fraction[1]
    a = a1; b = b1

    r = a % b
    while r != 0:
        a = b
        b = r
        r = a % b
    return [a1//b, b1//b]


closest_numerator = lambda denominator, target: int((denominator*target[0] - 1)
                                                    / target[1])

target = [3, 7]
numerator = 0
difference = 1.0

for i in range(3, 10**6 + 1):
    fraction = reduce([closest_numerator(i, target), i])
    if target[0]/target[1] - fraction[0]/fraction[1] < difference:
        numerator = fraction[0]
        difference = target[0]/target[1] - fraction[0]/fraction[1]
print(numerator)
print(difference)
