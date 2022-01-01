"""Day 22: Reactor Reboot

https://adventofcode.com/2021/day/22

"""
import re

CUBOID = r'(on|off) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)'


class Cuboid:

    def __init__(self, values):
        self.on = values[0] == 'on'
        self.x = (int(values[1]), int(values[2]))
        self.y = (int(values[3]), int(values[4]))
        self.z = (int(values[5]), int(values[6]))
        self.overlaps = []
        self.overlap_cuboids = []
        self.overlap_v = None
        self.total_volume = None

    def __repr__(self):
        return (
            f'{"on" if self.on else "off"}: '
            f'{self.x[0]}..{self.x[1]}, '
            f'{self.y[0]}..{self.y[1]}, '
            f'{self.z[0]}..{self.z[1]}'
        )

    @property
    def volume(self):
        return (
            (abs(self.x[1] - self.x[0]) + 1) *
            (abs(self.y[1] - self.y[0]) + 1) *
            (abs(self.z[1] - self.z[0]) + 1)
        )

    def calculate_overlap_v(self):
        if len(self.overlaps) == 0:
            self.overlap_v = 0
            return 0

        for i in self.overlaps:
            new_cuboid = create_cuboid_from_overlap(self, i)
            for c in self.overlap_cuboids:
                if is_overlap(c, new_cuboid):
                    c.overlaps.append(new_cuboid)
            self.overlap_cuboids.append(new_cuboid)

        self.overlap_v = sum([
            c.calculate_total_volume()
            for c in self.overlap_cuboids
        ])
        return self.overlap_v

    def calculate_total_volume(self):
        if self.total_volume:
            return self.total_volume
        if not self.overlap_v:
            self.calculate_overlap_v()
        self.total_volume = self.volume - self.overlap_v
        return self.total_volume


def parse(data, only_small=True):
    cuboids = []

    for values in re.findall(CUBOID, data):
        new_cuboid = Cuboid(values)
        for c in cuboids:
            if is_overlap(c, new_cuboid):
                c.overlaps.append(new_cuboid)
        if new_cuboid.on:
            cuboids.append(new_cuboid)

    if only_small:
        return clean_cuboids(cuboids)
    return cuboids


def clean_cuboid(cuboid):
    for attr in ('x', 'y', 'z'):
        start, stop = getattr(cuboid, attr)
        if start < -50 and stop < -50:
            return None
        elif start < -50 <= stop:
            setattr(cuboid, attr, (-50, stop))
        elif start > 50 and stop > 50:
            return None
        elif start <= 50 < stop:
            setattr(cuboid, attr, (start, 50))
    return cuboid


def clean_cuboids(cuboids):
    return list(filter(None, [clean_cuboid(c) for c in cuboids]))


def _dimension_overlap(cuboid1_x, cuboid2_x):
    if cuboid1_x[0] <= cuboid2_x[0] <= cuboid1_x[1]:
        return True
    if cuboid1_x[0] <= cuboid2_x[1] <= cuboid1_x[1]:
        return True
    if cuboid2_x[0] <= cuboid1_x[0] <= cuboid2_x[1]:
        return True
    if cuboid2_x[0] <= cuboid1_x[1] <= cuboid2_x[1]:
        return True
    return False


def is_overlap(cuboid1, cuboid2):
    return all([
        _dimension_overlap(cuboid1.x, cuboid2.x),
        _dimension_overlap(cuboid1.y, cuboid2.y),
        _dimension_overlap(cuboid1.z, cuboid2.z),
    ])


def create_cuboid_from_overlap(main_cuboid, overlap_cuboid):
    """
    a1...b1...b2...a2 -> b1...b2
    b1...a1...b2...a2 -> a1...b2
    a1...b1...a2...b2 -> b1...a2
    b1...a1...a2...b2 -> a1...a2
    """
    values = [overlap_cuboid.on]
    for d in ['x', 'y', 'z']:
        a1, a2 = getattr(main_cuboid, d)
        b1, b2 = getattr(overlap_cuboid, d)
        if a1 <= b1 and b2 <= a2:
            values.append(b1)
            values.append(b2)
        elif b1 <= a1 and b2 <= a2:
            values.append(a1)
            values.append(b2)
        elif a1 <= b1 and a2 <= b2:
            values.append(b1)
            values.append(a2)
        elif b1 <= a1 and a2 <= b2:
            values.append(a1)
            values.append(a2)
    c = Cuboid(values)
    return c


def solve(data, only_small=True):
    cuboids = parse(data, only_small)
    return sum(c.calculate_total_volume() for c in cuboids)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, True)
    print(f'Example1: {result}')

    result = solve(input_data, False)
    print(f'Example2: {result}')
