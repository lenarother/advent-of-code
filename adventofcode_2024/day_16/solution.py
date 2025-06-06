"""Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16

"""
import heapq

NEIGHBORS = [
                 ((0, -1), 'N'),               # noqa N
    ((-1, 0), 'W'),            ((1, 0), 'E'),  # noqa W E
                 ((0,  1), 'S'),               # noqa S
]

DIRECTIONS = 'NWSE'


def is_single_rotation(direction, new_direction):
    return (
        DIRECTIONS.index(direction) % 2 != DIRECTIONS.index(new_direction) % 2
    )


def neighbors(p, direction):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for n in NEIGHBORS:
        position, new_direction = n
        dx, dy = position
        if direction == new_direction:
            cost = 1
        elif is_single_rotation(direction, new_direction):
            cost = 1001
        else:
            cost = 2001
        yield ((x + dx, y + dy), new_direction, cost)


def get_grid_dict(data):
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def get_position(grid, ch='S'):
    for k, v in grid.items():
        if v == ch:
            return k


def solve(data):
    grid = get_grid_dict(data)
    start = get_position(grid, 'S')
    end = get_position(grid, 'E')
    direction = 'E'

    visited = set()
    unvisited = []
    heapq.heappush(unvisited, (0, (start, direction)))

    while unvisited:
        price, current_node = heapq.heappop(unvisited)
        p, direction = current_node
        if p == end:
            return price
        if p not in visited:
            visited.add(p)
            for n, new_direction, cost in neighbors(p, direction):
                if grid[n] in '.E':
                    new_price = price + cost
                    heapq.heappush(unvisited, (new_price, (n, new_direction)))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
