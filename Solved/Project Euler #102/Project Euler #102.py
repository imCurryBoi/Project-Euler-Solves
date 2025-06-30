area = lambda x0, x1, x2, y0, y1, y2: \
    0.5*abs(((x0 - x2) * (y1 - y0)) - ((x0 - x1) * (y2 - y0)))


miniarea = lambda x0, x1, y0, y1: 0.5*abs(x0*y1 - x1*y0)


def read_file(name):
    answer = 0
    with open('triangles.txt', 'r') as file:
        for line in file:
            line = line.split(',')
            a = area(int(line[0]), int(line[2]), int(line[4]), int(line[1]),
                     int(line[3]), int(line[5]))

            a1 = miniarea(int(line[0]), int(line[2]), int(line[1]), 
                          int(line[3]))

            a2 = miniarea(int(line[0]), int(line[4]), int(line[1]),
                          int(line[5]))

            a3 = miniarea(int(line[2]), int(line[4]), int(line[3]), 
                          int(line[5]))
            if a == a1 + a2 + a3:
                answer += 1
    return answer


print(read_file('triangles.txt'))
