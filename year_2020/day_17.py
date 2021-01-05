"""Day 17: Conway Cubes

https://adventofcode.com/2020/day/17

"""


def read_input(filename):
    data = {}
    f = open(filename).read().strip().split('\n')
    for y, l in enumerate(f):
        for x, point in enumerate(l):
            value = (1 if point == '#' else 0)
            data[(x, y)] = value
    return data


def get_initial_cube(data, size=3):
    cube = {}

    # Part 1: x, y, z
    if size == 3:
        for k in data:
            cube[(k[0], k[1], 0)] = data[k]
            cube[(k[0], k[1], 1)] = 0
            cube[(k[0], k[1], -1)] = 0

    # Part 2: x, y, z, w
    elif size == 4:
        for k in data:
            cube[(k[0], k[1], 0, 0)] = data[k]
            cube[(k[0], k[1], 1, 0)] = 0
            cube[(k[0], k[1], -1, 0)] = 0

            cube[(k[0], k[1], 0, 1)] = 0
            cube[(k[0], k[1], 1, 1)] = 0
            cube[(k[0], k[1], -1, 1)] = 0

            cube[(k[0], k[1], 0, -1)] = 0
            cube[(k[0], k[1], 1, -1)] = 0
            cube[(k[0], k[1], -1, -1)] = 0

    return cube


def get_coords(point, size=3):
    for x in range(point[0] - 1, point[0] + 2):
        for y in range(point[1] - 1, point[1] + 2):
            for z in range(point[2] - 1, point[2] + 2):
                if size == 3:
                    # Part 1
                    yield (x, y, z)
                elif size == 4:
                    for w in range(point[3] - 1, point[3] + 2):
                        # Part 2
                        yield (x, y, z, w)


def get_new_neighbors(point, data, size=3):
    new_data = {}
    coords = get_coords(point, size)
    for coord in coords:
        if coords != point and coord not in data:
            new_data[coord] = 0
    return new_data


def get_active_neighbour_count(point, data, size=3):
    result = 0
    coords = get_coords(point, size)
    for coord in coords:
        if coord != point and coord in data and data[coord]:
            result += 1
    return result


def update_data_with_new_elements(data, size=3):
    new_elements = {}
    for el in data:
        new_neighbors = get_new_neighbors(el, data, size)
        new_elements.update(new_neighbors)
    data.update(new_elements)
    return data


def simulate_step(data, size=3):
    changed_data = {}
    data = update_data_with_new_elements(data, size)

    for point in data:
        active_neighbours = get_active_neighbour_count(point, data, size)
        if data[point] == 1 and not (active_neighbours == 2 or active_neighbours == 3):
            changed_data[point] = 0
        if data[point] == 0 and active_neighbours == 3:
            changed_data[point] = 1

    data.update(changed_data)
    return data


def simulate(filename, steps=6, size=3):
    data = read_input(filename)
    data = get_initial_cube(data, size)

    while steps:
        data = simulate_step(data, size)
        steps = steps - 1

    return sum(list(data.values()))


def print_cube(cube):
    # Debug part 1
    keys = sorted(list(cube.keys()))
    min_el = keys[0]
    max_el = keys[-1]

    for z in range(min_el[2], max_el[2] + 1):
        print(f'z={z}')
        for y in range(min_el[1], max_el[1] + 1):
            l = [str(cube[x, y, z]) for x in range(min_el[0], max_el[0] + 1)]
            print(''.join(l))
        print('\n')


if __name__ == '__main__':

    # Part 1
    result = simulate('inputdata/day-17-2.txt', 6, 3)
    print('Part 1 - Result: ', result)

    # Part 2
    result = simulate('inputdata/day-17-2.txt', 6, 4)
    print('Part 2 - Result: ', result)
