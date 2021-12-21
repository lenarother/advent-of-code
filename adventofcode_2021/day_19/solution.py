"""Day 19: Beacon Scanner

https://adventofcode.com/2021/day/19

"""
import math
import re

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


def rotations():
    for o_rule in ORIENTATION_RULES:
        x, y, z = o_rule
        for c_rule in CASTING_RULES:
            v1, v2, v3 = c_rule
            yield (
                lambda p: (p[x] * v1, p[y] * v2, p[z] * v3)
            )


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


class Scanner:

    def __init__(self, id, points):
        self.id = id
        self.points = points
        self.distance_matrix = get_dist_matrix(points)
        self.partners = []
        self.rotated = False

    def __repr__(self):
        return f'<Scanner: {self.id}>'

    def overlaps(self, s2):
        for row in self.distance_matrix:
            for row_other in s2.distance_matrix:
                if len(set(row).intersection(set(row_other))) >= 12:
                    self.partners.append(s2)
                    return True
        return False

    def rotate(self, rotation, vector):
        self.points = apply_rotation_vector(self.points, rotation, vector)
        self.rotated = True


def get_vector(target_p, p):
    tx, ty, tz = target_p
    x, y, z = p
    return tx - x, ty - y, tz - z


def apply_rotation_vector(points, rotation, vector):
    new_points = []
    for p in points:
        x, y, z = rotation(p)
        v1, v2, v3 = vector
        new_points.append((x + v1, y + v2, z + v3))
    return new_points


def find_vector(target_s, s):
    for target_p in target_s.points:
        for p in s.points:
            for rotation in rotations():
                new_p = rotation(p)
                v = get_vector(target_p, new_p)
                new_points = apply_rotation_vector(s.points, rotation, v)
                if len(set(target_s.points).intersection(set(new_points))) >= 12:
                    return rotation, v


def match_scanners(scanners):
    for id, s in scanners.items():
        for id_other, s_other in scanners.items():
            if id == id_other:
                continue
            s.overlaps(s_other)


def parse(data):
    scanners = {}
    for scanner in data.strip().split('\n\n'):
        scanner_data = scanner.strip().split('\n')
        scanner_id = re.findall(r'--- scanner (\d+) ---', scanner_data[0])[0]
        scanner_points = [
            tuple(map(int, line.strip().split(',')))
            for line in scanner_data[1:]
        ]
        # scanners[int(scanner_id)] = {(0, 0, 0): scanner_points}
        scanners[int(scanner_id)] = Scanner(int(scanner_id), scanner_points)
    return scanners


def get_beacons(data):
    scanners = parse(data)
    match_scanners(scanners)

    s0 = scanners[0]
    s0.rotated = True
    to_do = [s0]
    while to_do:
        s = to_do.pop()
        for partner in s.partners:
            if not partner.rotated:
                r, v = find_vector(s, partner)
                partner.rotate(r, v)
                to_do.append(partner)

    beacons = []
    for s in scanners.values():
        beacons += s.points

    return set(beacons)


def solve(data):
    beacons = get_beacons(data)
    return len(beacons)


def get_max_dist(beacons):
    distances = []
    for p1 in beacons:
        x1, y1, z1 = p1
        for p2 in beacons:
            x2, y2, z2 = p2
            distances.append(
                abs(x1 - x2) + abs(y1 - y2) + abs(z1 - z2)
            )
    return max(distances)


def solve2(data):
    vectors = []
    scanners = parse(data)
    match_scanners(scanners)

    s0 = scanners[0]
    s0.rotated = True
    to_do = [s0]
    while to_do:
        s = to_do.pop()
        for partner in s.partners:
            if not partner.rotated:
                r, v = find_vector(s, partner)
                vectors.append(v)
                partner.rotate(r, v)
                to_do.append(partner)

    return get_max_dist(vectors)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
