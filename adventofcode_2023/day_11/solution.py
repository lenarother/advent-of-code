"""Day 11: Cosmic Expansion

https://adventofcode.com/2023/day/11

"""
import itertools

from santa_helpers.parse import parse_grid_to_dict  # type: ignore


def column_count(data: str) -> int:
    return len(data.strip().split('\n')[0])


def row_count(data: str) -> int:
    return int(
        len(data.strip().replace('\n', '')) /
        len(data.strip().split('\n')[0])
    )


def get_empty_rows_and_columns(
        grid: dict[tuple[int, int], str],
        data: str
) -> tuple[set[int], set[int]]:
    occupied_columns = set([x for (x, y), v in grid.items() if v == '#'])
    occupied_rows = set([y for (x, y), v in grid.items() if v == '#'])

    empty_columns = set(range(0, column_count(data))) - occupied_columns
    empty_rows = set(range(0, row_count(data))) - occupied_rows

    return empty_rows, empty_columns


def get_distance(
        a: tuple[int, int],
        b: tuple[int, int],
        empty_rows: set[int],
        empty_columns: set[int],
        n: int = 1  # expansion_factor
) -> int:
    """Get Manhattan distance between two points including grid expansion."""
    min_x, max_x = sorted([a[0], b[0]])
    min_y, max_y = sorted([a[1], b[1]])

    expanded_rows = n * len(empty_rows.intersection(range(min_y, max_y)))
    expanded_column = n * len(empty_columns.intersection(range(min_x, max_x)))

    manhattan_dist = (max_x - min_x) + (max_y - min_y)
    return manhattan_dist + expanded_rows + expanded_column


def solve(data: str, n: int = 1) -> int:
    grid = parse_grid_to_dict(data)
    points = [k for k, v in grid.items() if v == '#']
    empty_rows, empty_columns = get_empty_rows_and_columns(grid, data)

    return sum([
        get_distance(pair[0], pair[1],  empty_rows, empty_columns, n)
        for pair in itertools.combinations(points, 2)
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, 1000000 - 1)
    print(f'Example2: {result}')
