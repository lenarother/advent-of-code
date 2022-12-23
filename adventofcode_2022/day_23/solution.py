"""Day 23: Unstable Diffusion

https://adventofcode.com/2022/day/23

"""

"""
NW-N-NE
|  | |
W----E
|  | |
SW-S-SE
"""
DIRECTIONS = {
    'N': (0, -1),
    'NW': (-1, -1),
    'NE': (1, -1),
    'W': (-1, 0),
    'E': (1, 0),
    'S': (0, 1),
    'SW': (-1, 1),
    'SE': (1, 1),
}


def parse(data):
    elfs = {}
    for y, row in enumerate(data.strip().split('\n')):
        for x, position in enumerate(row):
            if position == '#':
                elfs[(x, y)] = position
    return elfs


def get_proposed_grid(elfs, directions):
    proposed_elfs = set()
    proposed_positions = []
    for elf in elfs:
        position = get_proposed_position(elf, elfs, directions)
        proposed_elfs.add((position, elf))
        proposed_positions.append(position)
    return proposed_elfs, proposed_positions


def apply_proposed_grid(proposed_elfs, proposed_positions):
    from collections import Counter
    proposed_counter = Counter(proposed_positions)
    new_elfs = {}
    for new_elf, old_elf in proposed_elfs:
        if proposed_counter[new_elf] > 1:
            new_elfs[old_elf] = 1
        else:
            new_elfs[new_elf] = 1
    return new_elfs


def proposed_directions():
    directions = 'NSWE'
    while True:
        yield directions
        directions = directions[1:] + directions[0]


def step(elfs, directions):
    proposed_elfs, proposed_positions = get_proposed_grid(elfs, directions)
    return apply_proposed_grid(proposed_elfs, proposed_positions)


def get_neighbours(elf, elfs):
    x, y = elf
    neighbours = {}
    for d, coord in DIRECTIONS.items():
        dx, dy = coord
        new_coord = x + dx, y + dy
        if new_coord in elfs:
            neighbours[d] = new_coord
    return neighbours


def get_adjacent_directions(d):
    """
    NW-N-NE
    |    |
    W----E
    |    |
    SW-S-SE
    """
    dirs = ['NW', 'N', 'NE', 'E', 'SE', 'S', 'SW', 'W']
    i = dirs.index(d)
    return dirs[i-1], d, dirs[(i+1) % len(dirs)]


def is_direction_valid(d, elf, elfs):
    x, y = elf
    for ad in get_adjacent_directions(d):
        dx, dy = DIRECTIONS[ad]
        if (x + dx, y + dy) in elfs:
            return False
    return True


def get_proposed_position(elf, elfs, directions):
    x, y = elf
    neighbours = get_neighbours(elf, elfs)
    if len(neighbours) == 0:
        return elf

    for d in directions:
        if is_direction_valid(d, elf, elfs):
            dx, dy = DIRECTIONS[d]
            return x + dx, y + dy

    return elf


def calculate_empty_area(elfs):
    all_x = [x for x, _ in elfs]
    all_y = [y for _, y in elfs]
    all_x.sort()
    all_y.sort()
    a = all_x[-1] - all_x[0] + 1
    b = all_y[-1] - all_y[0] + 1
    occupied = len(elfs)
    return (a * b) - occupied


def solve(data, n=10):
    elfs = parse(data)
    proposed_directions_gen = proposed_directions()
    while n:
        n -= 1
        directions = next(proposed_directions_gen)
        elfs = step(elfs, directions)
    return calculate_empty_area(elfs)


def solve2(data):
    elfs = {}
    new_elfs = parse(data)
    proposed_directions_gen = proposed_directions()
    n = 0
    while elfs != new_elfs:
        n += 1
        elfs = new_elfs
        directions = next(proposed_directions_gen)
        new_elfs = step(elfs, directions)
    return n


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
