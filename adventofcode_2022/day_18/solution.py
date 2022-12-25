"""Day 18: Boiling Boulders

https://adventofcode.com/2022/day/18

"""
import re
CUBE_RE = re.compile(r'(\d+),(\d+),(\d+)\n')


def get_coord(x, y, z):
    return {
        (x, y, z),
        (x+1, y+1, z+1),
        (x, y, z+1),
        (x+1, y, z),
        (x, y+1, z),
        (x+1, y, z+1),
        (x+1, y+1, z),
        (x, y+1, z+1),
    }


def connected(cube, other_cube):
    return sum([abs(i - j) for i, j in zip(cube, other_cube)]) <= 1


def get_cubes_dicts(data, coord_function=get_coord):
    cubes = {}
    connections = {}
    for x, y, z in CUBE_RE.findall(data):
        x, y, z = int(x), int(y), int(z)
        cubes[(x, y, z)] = coord_function(x, y, z)
        connections[(x, y, z)] = 0
    return cubes, connections


def get_cubes(data):
    return [(int(x), int(y), int(z)) for x, y, z in CUBE_RE.findall(data)]


def solve(data):
    cubes, connections = get_cubes_dicts(data)
    for cube in connections:
        coord = cubes.pop(cube)
        for other, other_coord in cubes.items():
            if len(coord & other_coord) == 4:  # faster
            # if connected(cube, other):  # slower
                connections[cube] += 1
                connections[other] += 1

    free_walls = 0
    for connection_count in connections.values():
        free_walls += 6 - connection_count

    return free_walls


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
