import numpy as np
from collections import Counter

playground = np.zeros((9,9))

test = [(2,3),(2,1)]

playground[test[0][1]][test[0][0]] = 1
playground[test[1][1]][test[1][0]] = 1

with open('AoC21/data/AoC_5_2021.in') as file:
    data = file.read().splitlines()


def part1():
    allPoints = []

    for line in data:
        #print(line)
        points = line.split('->')
        x1,y1 = tuple(map(int, points[0].split(',')))
        x2, y2 = tuple(map(int, points[1].split(',')))

        if x1 == x2 or y1 == y2:
            for x in range(min(x1,x2), max(x1,x2)+1):
                for y in range(min(y1,y2), max(y1,y2)+1):
                    allPoints.append((x,y))
    return len([point for point in Counter(allPoints).values() if point > 1])


print('Part1: Number of overlappint points is:', part1())
