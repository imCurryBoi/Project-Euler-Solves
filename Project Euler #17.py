def convert(n):
    ones = [0,3,3,5,4,4,3,5,5,4]
    tens = [0,3,6,6,5,5,5,7,6,6]
    teens = [3,6,6,8,8,7,7,9,8,8]

    if n == 1000:
        return 11

    if n >= 100:
        if n % 100 == 0:
            return ones[n//100] + 7
        return convert(n % 100) + ones[n // 100] + 7 + 3
    if n >= 20:
        return ones[n % 10] + tens[n // 10]
    if n >= 10:
        return teens[n % 10]
    return ones[n]

counter = 0

for i in range(1, 1001):
    counter += convert(i)

print(counter)