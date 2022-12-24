"""Day 22: Monkey Map

https://adventofcode.com/2022/day/22

        >>v#
        .#v.
        #.v.
        ..v.
...#...v..v#
>>>v...>#.>>
..#v...#....
...>>>>v..#.
        ...#....
        .....#..
        .#......
        ......#.

10R5L5R10L4R5L5
"""


def get_direction(current_direction, orientation):
    directions = [(1, 0), (0, 1), (-1, 0), (0, -1)]
    i = directions.index(current_direction)
    new_i = i + (1 if orientation == 'R' else -1)
    new_i = new_i % 4 if new_i >= 4 else new_i
    return directions[new_i]


def parse_area(data):
    area = data.strip('\n')
    area_map = {}
    for y, row in enumerate(area.split('\n')):
        for x, position in enumerate(row):
            if position in '.#':
                area_map[(x + 1, y + 1)] = position
    import pprint
    pprint.pprint(area_map)
    return area_map


def parse_moves(moves):
    moves_list = []
    moves = moves.strip()
    current_move = moves[0]
    for m in moves[1:]:

        if current_move.isdigit():
            if m.isdigit():
                current_move += m
            else:
                moves_list.append(int(current_move))
                current_move = m

        elif current_move in 'RL':
            moves_list.append(current_move)
            current_move = m

    # append last element
    moves_list.append(
        current_move
        if current_move in 'LR' else int(current_move)
    )
    return moves_list


def parse(data):
    area, moves = data.split('\n\n')
    area_map = parse_area(area)
    moves_list = parse_moves(moves)
    return area_map, moves_list


def find_opposite(position, direction, positions):
    x, y = position
    all_x = [i[0] for i in positions if i[1] == y]
    all_y = [i[1] for i in positions if i[0] == x]
    if direction == (1, 0):
        return min(all_x), y
    elif direction == (0, 1):
        return x, min(all_y)
    elif direction == (-1, 0):
        return max(all_x), y
    elif direction == (0, -1):
        return x, max(all_y)


def get_result(position, direction):
    column, row = position
    direction_points = {
        (1, 0): 0,  # >
        (0, 1): 1,  # v
        (-1, 0): 2,  # <
        (0, -1): 3,  # ^
    }
    return 4 * column + 1000 * row + direction_points[direction]


def get_start_position(area):
    """Leftmost open tile of the top row of tiles."""
    all_x = [x for x, y in area if y == 1]
    y = 1
    all_x.sort()
    for x in all_x:
        if area[(x, y)] == '.':
            return x, y


def solve(data):
    area, moves = parse(data)
    position = get_start_position(area)
    direction = (1, 0)
    for m in moves:
        if isinstance(m, int):
            steps = 0
            while steps < m:
                position = go(position, direction, area)
                steps += 1
        else:
            direction = get_direction(direction, m)
    return get_result(position, direction)


def go(current_position, direction, area_map):
    x, y = current_position
    dx, dy = direction
    nx, ny = x + dx, y + dy
    if (nx, ny) in area_map:
        candidate = (nx, ny)
    else:
        candidate = find_opposite(current_position, direction, area_map)
    if area_map[candidate] == '.':
        return candidate
    return x, y


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
