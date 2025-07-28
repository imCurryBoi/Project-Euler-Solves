from math import log


def which_bigger(ex1, ex2):
    return ex1[1] * log(ex1[0]) < ex2[1] * log(ex2[0])


def read_file():
    f = []
    with open('exp.txt', 'r') as file:
        for line in file:
            line = line.split(',')
            line[0] = int(line[0])
            line[1] = int(line[1])
            f.append(line)
    return f


file = read_file()
c = file[0]
line = None

for i in range(1, len(file)):
    if which_bigger(c, file[i]):
        c = file[i]
        line = i + 1

print(line)
print(c)
