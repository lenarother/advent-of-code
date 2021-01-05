"""Day 24: Lobby Layout

https://adventofcode.com/2020/day/24

"""

DIRECTION = {
    'e': (1, 0),
    'se': (0.5, 1),
    'sw': (-0.5, 1),
    'w': (-1, 0),
    'nw': (-0.5, -1),
    'ne': (0.5, -1),
}


def parse_rule(rule, result=None):
    if result is None:
        result = []
    if len(rule) == 0:
        return result
    if rule[0] in ['s', 'n']:
        result.append(rule[:2])
        return parse_rule(rule[2:], result)
    result.append(rule[:1])
    return parse_rule(rule[1:], result)


def parse_input(filename):
    data = []
    for line in open(filename).read().strip().split('\n'):
        data.append(parse_rule(line))
    return data


def get_tile(data):
    x = 0
    y = 0
    for direction in data:
        dx, dy = DIRECTION[direction]
        x += dx
        y += dy
    return x, y


def flip(data):
    result = {}
    for x in data:
        tile = get_tile(x)
        result.setdefault(tile, 0)
        result[tile] += 1
    return result


def count_black_tiles(filename):
    # Part 1
    data = parse_input(filename)
    result = flip(data)
    return sum(x % 2 for x in result.values())


def get_count_of_black_neighbours(tile, data):
    neighbours = []
    for dx, dy in DIRECTION.values():
        x = tile[0] + dx
        y = tile[1] + dy
        if (x, y) in data:
            neighbours.append(data[(x, y)])
    return sum(x % 2 for x in neighbours)


def add_missing_neighbours(data):
    to_add = {}
    for tile in data:
        for dx, dy in DIRECTION.values():
            x = tile[0] + dx
            y = tile[1] + dy
            if (x, y) not in data:
                to_add.setdefault((x, y), 0)
    data.update(to_add)
    return data


def simulate_round(data):
    data = add_missing_neighbours(data)
    to_flip = []

    for tile in data:
        is_black = data[tile] % 2
        black_neighbours = get_count_of_black_neighbours(tile, data)
        if (
            (is_black and black_neighbours > 2)
            or (is_black and black_neighbours == 0)
            or (not is_black and black_neighbours == 2)
        ):
            to_flip.append(tile)

    for tile in to_flip:
        data[tile] += 1

    return data


def simulate(filename, rounds=100):
    # Part 2
    data = parse_input(filename)
    tiles = flip(data)
    while rounds:
        tiles = simulate_round(tiles)
        rounds = rounds - 1
    return sum(x % 2 for x in tiles.values())


if __name__ == '__main__':

    # Part 1
    result = count_black_tiles('inputdata/day-24-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = count_black_tiles('inputdata/day-24-2.txt')
    print('Part 1 - Result: ', result)

    # Part 2
    result = simulate('inputdata/day-24-1.txt', 100)
    print('Part 2 - Test set 1: ', result)

    result = simulate('inputdata/day-24-2.txt', 100)
    print('Part 2 - Result: ', result)
