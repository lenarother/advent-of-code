"""Day 16: The Floor Will Be Lava

https://adventofcode.com/2023/day/16

"""
from santa_helpers.parse import parse_grid_to_dict  # type: ignore

MOVES = {
    'R': (1, 0),
    'L': (-1, 0),
    'U': (0, -1),
    'D': (0, 1),
}

ROTATE_LEFT = {
    'L': 'D',
    'R': 'U',
    'U': 'R',
    'D': 'L'
}

ROTATE_RIGHT = {
    'L': 'U',
    'R': 'D',
    'U': 'L',
    'D': 'R'
}


def column_count(data: str) -> int:
    return len(data.strip().split('\n')[0])


def row_count(data: str) -> int:
    return int(
        len(data.strip().replace('\n', '')) /
        len(data.strip().split('\n')[0])
    )


def get_single_move(
    point: tuple[int, int],
    direction: str,
    grid: dict,
    visited: set[tuple[tuple[int, int], str]]
):
    x = point[0]
    y = point[1]

    move = MOVES[direction]
    new_point = x + move[0], y + move[1]

    if new_point not in grid:
        return None

    new_move = new_point, direction
    if new_move in visited:
        return None

    return new_move


def get_next_move(
    current: tuple[tuple[int, int], str],
    grid: dict[tuple[int, int], str],
    visited: set[tuple[tuple[int, int], str]]
):
    point = current[0]
    direction = current[1]

    if grid[point] == '.':
        move = get_single_move(point, direction, grid, visited)
        return move, None

    elif grid[point] == '|':
        if direction in 'DU':
            move = get_single_move(point, direction, grid, visited)
            return move, None

        elif direction in 'RL':
            # split
            move_up = get_single_move(point, 'U', grid, visited)
            move_down = get_single_move(point, 'D', grid, visited)
            return move_up, move_down

    elif grid[point] == '-':
        if direction in 'LR':
            move = get_single_move(point, direction, grid, visited)
            return move, None

        elif direction in 'UD':
            # split
            move_left = get_single_move(point, 'L', grid, visited)
            move_right = get_single_move(point, 'R', grid, visited)
            return move_left, move_right

    elif grid[point] == r'/':
        new_direction = ROTATE_LEFT[direction]
        move = get_single_move(point, new_direction, grid, visited)
        return move, None

    else:
        # \
        new_direction = ROTATE_RIGHT[direction]
        move = get_single_move(point, new_direction, grid, visited)
        return move, None


def solve(data: str, first_point: tuple[tuple[int, int], str]):
    grid = parse_grid_to_dict(data.strip())
    starts = {first_point}
    visited = set()

    while starts:
        next_move = starts.pop()
        while next_move:
            visited.add(next_move)
            next_move, new_start = get_next_move(next_move, grid, visited)
            if new_start:
                starts.add(new_start)

    return len(set([i[0] for i in visited]))


def solve_all(data: str) -> int:
    n_columns = column_count(data)
    n_rows = row_count(data)
    starts = (
        # top edge
        [((i, 0), 'D') for i in range(0, n_columns)] +
        # down edge
        [((i, n_rows - 1), 'U') for i in range(0, n_columns)] +
        # left edge
        [((0, i), 'D') for i in range(0, n_rows)] +
        # right edge
        [((n_rows - 1, i), 'D') for i in range(0, n_rows)]
    )
    return max([solve(data, start) for start in starts])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, ((0, 0), 'R'))
    print(f'Example1: {result}')

    result = solve_all(input_data)
    print(f'Example2: {result}')
