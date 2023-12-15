"""Day 14: Parabolic Reflector Dish

https://adventofcode.com/2023/day/14

"""


def column_count(data: str) -> int:
    return len(data.strip().split('\n')[0])


def row_count(data: str) -> int:
    return int(
        len(data.strip().replace('\n', '')) /
        len(data.strip().split('\n')[0])
    )


def parse_grid_to_dict(data: str, row_count: int) -> dict:
    """
    Parse grid given as a string to dictionary.
    k: coordinates (x, y) (y coordinate is reversed)
    v: value

    Example:
        X.O    =>   { (0, 2): 'X', (1, 2): '.', (2, 2): 'O',
        ...           (0, 1): '.', (1, 1): '.', (2, 1): '.',
        ..O           (0, 0): '.', (1, 0): '.', (2, 0): 'O', }

    """
    return {
        (x, y): v

        for y, row
        in zip((range(row_count, 0, -1)), (data.strip().split('\n')))

        for x, v
        in enumerate(row.strip())
    }


def print_grid(grid: dict) -> None:
    grid_string = "\n"
    for y in range(1, 11):
        for x in range(0, 10):
            if (x, y) in grid:
                grid_string += grid[(x, y)]
            else:
                grid_string += '.'
        grid_string += '\n'
    print(grid_string)


def round_rocks(grid: dict):
    rocks = [k for k, v in grid.items() if v == 'O']
    rocks.sort(key=lambda x: x[1])
    while rocks:
        yield rocks.pop()


def get_new_coord(
    point: tuple[int, int],
    grid: dict
) -> tuple[int, int] | None:
    new_point = (point[0], point[1] + 1)
    if new_point in grid and grid[new_point] == '.':
        return new_point
    return None


def solve(data: str) -> int:
    grid = parse_grid_to_dict(data, row_count(data))
    for rock in round_rocks(grid):
        grid.pop(rock)
        grid[rock] = '.'
        pre_coord = rock
        new_coord = rock

        while new_coord:
            new_coord = get_new_coord(new_coord, grid)
            if new_coord:
                pre_coord = new_coord

        grid[pre_coord] = 'O'

    return sum([i[1] for i in round_rocks(grid)])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')
