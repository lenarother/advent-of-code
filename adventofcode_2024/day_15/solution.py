"""Day 15: Warehouse Woes

https://adventofcode.com/2024/day/15

"""
DIRECTIONS = {
    '<': (-1, 0),
    '>': (1, 0),
    'v': (0, 1),
    '^': (0, -1),
}


def get_grid_dict(data):
    data = data.strip().split('\n\n')[0]
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }

def get_grid_size(grid):
    a = list(grid.keys())
    a.sort()
    x, y = a[-1]
    return x + 1, y + 1
    #data = data.strip().split('\n\n')[0]
    #data = data.strip().split('\n')
    #x = len(data[0])
    #y = len(data)
    #return x, y


def moves_gen(data):
    data = data.strip().split('\n\n')[1]
    data = data.replace('\n', '')
    for i in data:
        yield i


def print_grid(grid, data):
    x, y = get_grid_size(grid)
    picture = ''
    for row in range(y):
        for column in range(x):
            picture += grid[(column, row)]
        picture += '\n'
    print(picture)


def get_initial_position(grid):
    for p, ch in grid.items():
        if ch == "@":
            start = p
    grid[start] = '.'
    return start

def apply_move(p, move, grid):
    x, y = p
    dx, dy = DIRECTIONS[move]
    nx = x + dx
    ny = y + dy
    np = (nx, ny)
    print(np)

    # wall
    if grid[np] == '#':
        print('MOVE: WALL')
        return p

    # free to go
    if grid[np] == '.':
        print('MOVE: CAN GO')
        return np

    # box
    if grid[np] == 'O':
        print('MOVE: BOX')
        foo = np
        chain_len = 0
        while grid[foo] == 'O':
            chain_len += 1
            foo_x, foo_y = foo
            foo = (foo_x + dx, foo_y + dy)
        if grid[foo] == '#':
            return p
        elif grid[foo] == '.':
            grid[np] = '.'
            grid[foo] = 'O'
        return np


def calculate_boxes_score(grid):
    result = 0
    for p, ch in grid.items():
        if ch == 'O':
            x, y = p
            result += (100 * y) + x
    return result

def solve(data):
    grid = get_grid_dict(data)
    moves = list(moves_gen(data))
    position = get_initial_position(grid)
    print_grid(grid, data)
    for m in moves:
        position = apply_move(position, m, grid)
    return calculate_boxes_score(grid)

def get_expanded_grid(data):
    data = data.replace('#', '##')
    data = data.replace('.', '..')
    data = data.replace('O', '[]')
    data = data.replace('@', '@.')
    return get_grid_dict(data)

def apply_move_2(p, move, grid):
    x, y = p
    dx, dy = DIRECTIONS[move]
    nx = x + dx
    ny = y + dy
    np = (nx, ny)
    print(np)

    # wall
    if grid[np] == '#':
        print('MOVE: WALL')
        return p

    # free to go
    if grid[np] == '.':
        print('MOVE: CAN GO')
        return np

    # box
    if grid[np] in '[]':
        print('MOVE: BOX')
        if move in '<>':
            print('LEFT - RIGHT')
            foo = np
            foo_x, foo_y = foo
            chain_len = 0
            while grid[foo] in '[]':
                chain_len += 1
                foo_x, foo_y = foo
                foo = (foo_x + dx, foo_y + dy)
            print('FOO', foo)
            if grid[foo] == '#':
                return p
            elif grid[foo] == '.':
                bar = np
                bar_x, bar_y = bar
                temp = '.'
                print('NEXT FOO', foo_x + dx + dx, foo_y + dy + dy)
                while bar != (foo_x + dx + dx, foo_y + dy + dy):
                    print('BAR', bar)
                    new_temp = grid[bar]
                    grid[bar] = temp
                    temp = new_temp
                    bar = (bar_x + dx, bar_y + dy)
                    bar_x, bar_y = bar
                return np

        if move in '^v':
            pass


def move_line(position, grid, dx, dy):
    chain_len = 0
    temp =
    while grid[position] in '[]':
        chain_len += 1
        foo_x, foo_y = position
        foo = (foo_x + dx, foo_y + dy)
    if grid[position] == '#':
        return p
    elif grid[foo] == '.':
        grid[np] = '.'
        grid[foo] = 'O'
    return np
def solve2(data):
    grid = get_expanded_grid(data)
    moves = list(moves_gen(data))
    position = get_initial_position(grid)
    print_grid(grid, data)
    for m in moves:
        position = apply_move_2(position, m, grid)
        print_grid(grid, data)
    #return calculate_boxes_score(grid)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
