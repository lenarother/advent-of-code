"""Day 19: Beacon Scanner

https://adventofcode.com/2021/day/19

"""
import math
import re
from collections import defaultdict
import pprint


ORIENTATION_RULES = [
    (0, 1, 2),
    (0, 2, 1),
    (1, 2, 0),
    (1, 0, 2),
    (2, 0, 1),
    (2, 1, 0),
]

CASTING_RULES = [
    (1, 1, 1),
    (-1, -1, -1),
    (1, -1, -1),
    (-1, 1, -1),
    (-1, -1, 1),
    (1, -1, 1),
    (-1, 1, 1),
    (1, 1, -1),
]

def check_orientations():
    result = {}
    pos = (1, 3, 5)
    for i in ORIENTATION_RULES:
        xo = pos[i[0]]
        yo = pos[i[1]]
        zo = pos[i[2]]
        for j in CASTING_RULES:
            x = xo * j[0]
            y = yo * j[1]
            z = zo * j[2]
            result[(i, j)] = (x, y, z)

    result2 = defaultdict(list)
    for k, v in result.items():
        result2[v].append(k)

    pprint.pprint(result2)


def distance(pos1, pos2):
    x1, y1, z1 = pos1
    x2, y2, z2 = pos2
    return round(math.sqrt(
        (x2 - x1) ** 2 +
        (y2 - y1) ** 2 +
        (z2 - z1) ** 2
    ))


def get_dist_matrix(positions):
    dm = []
    for p in positions:
        dp = []
        for p2 in positions:
            dp.append(distance(p, p2))
        dm.append(dp)
    return dm


def get_dm_repr(dm):
    dm_repr = ''
    for row in dm:
        dm_repr += ', '.join(str(d) for d in row) + '\n'
    return dm_repr


class Scanner:

    def __init__(self, id, points):
        self.id = id
        self.points = points
        self.oriented_points = None

        self.casted_points = defaultdict(list)
        self.cast()

        self.dm = {}
        self.calc_dist_matrix()

        self.partner = None
        self.relation = None

    def cast(self):
        for pos in self.points:
            for i in ORIENTATION_RULES:
                ox = pos[i[0]]
                oy = pos[i[1]]
                oz = pos[i[2]]
                for j in CASTING_RULES:
                    x = ox * j[0]
                    y = oy * j[1]
                    z = oz * j[2]
                    self.casted_points[(i, j)].append((x, y, z))

    def calc_dist_matrix(self):
        for k, v in self.casted_points.items():
            self.dm[k] = get_dist_matrix(v)

    def overlaps(self, s2):
        point = None
        matrix = self.dm[((0, 1, 2), (1, 1, 1))]
        #for orientation, matrix in self.dm.items():
        for orientation_other, matrix_other in s2.dm.items():
            for enum, row in enumerate(matrix):
                for enum_other, row_other in enumerate(matrix_other):
                    common_distances = set(row).intersection(set(row_other))
                    if len(common_distances) >= 12:
                        print(orientation_other, s2.points[enum_other], self.points[enum])
                        #print(True)
                        #return orientation_other, s2.points[enum_other], self.points[enum]

        return None, None







def parse(data):
    scanners = {}
    for scanner in data.strip().split('\n\n'):
        scanner_data = scanner.strip().split('\n')
        scanner_id = re.findall(r'--- scanner (\d+) ---', scanner_data[0])[0]
        scanner_points = [
            list(map(int, line.strip().split(',')))
            for line in scanner_data[1:]
        ]
        # scanners[int(scanner_id)] = {(0, 0, 0): scanner_points}
        scanners[int(scanner_id)] = Scanner(int(scanner_id), scanner_points)
    return scanners


def solve(data):
    scanners = parse(data)

    s0 = scanners[0]
    s1 = scanners[1]
    print(s0.overlaps(s1))
    #check_orientations()
    return data


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
#
# T -618,-824,-621
# 686,422,578
#
# 686 * (-1) + 68
# 422 * (1) +