"""Day 20: Race Condition

https://adventofcode.com/2024/day/20

"""

NEIGHBORS = [
    (0, -1),  # noqa
    (-1, 0),
    (1, 0),  # noqa
    (0, 1),  # noqa
]


def neighbors(p):
    """Point neighbor generator.

    Yields:
        point (x, y)
    """
    x, y = p
    for dx, dy in NEIGHBORS:
        yield x + dx, y + dy


def get_grid_dict(data):
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split("\n"))
        for x, v in enumerate(row.strip())
    }


def get_max_point(grid):
    return sorted(list(grid.keys()))[-1]


def get_point(grid, ch="S"):
    for k, v in grid.items():
        if v == ch:
            return k


def in_grid(p, max_p):
    x, y = p
    max_x, max_y = max_p
    return 0 <= x <= max_x and 0 <= y <= max_y


def is_wall(p, max_p):
    x, y = p
    max_x, max_y = max_p
    if x == max_x or y == max_y:
        return True
    return False


def get_path(grid, start, end, max_p, collect_walls=True):
    walls = []
    paths = [(start, 0)]
    visited = []
    while paths:
        current, length = paths.pop(0)
        if current == end:
            return length, walls
        else:
            for n in neighbors(current):
                if grid[n] != "#" and in_grid(n, max_p) and n not in visited:
                    paths.append((n, length + 1))
                    visited.append(n)
                if (
                    collect_walls
                    and grid[n] == "#"
                    and in_grid(n, max_p)
                    and not is_wall(n, max_p)
                ):
                    walls.append(n)


def get_cheating_path(grid, start, end, max_p, cheat):
    ready = []
    paths = [(start, 0)]
    visited = []
    while paths:
        current, length = paths.pop(0)
        if current == end:
            ready.append(length)
        else:
            for n in neighbors(current):
                if (
                    in_grid(n, max_p)
                    and (n == cheat or grid[n] != "#")
                    and n not in visited
                ):
                    paths.append((n, length + 1))
                    visited.append(n)
    return min(ready)


def solve(data):
    from collections import Counter

    grid = get_grid_dict(data)
    max_p = get_max_point(grid)
    start = get_point(grid, "S")
    end = get_point(grid, "E")
    length, walls = get_path(grid, start, end, max_p)
    walls = set(walls)
    cheat_lengths = []
    counter = 0
    for i in walls:
        counter += 1
        cheat_length = get_cheating_path(grid, start, end, max_p, i)
        cheat_lengths.append(cheat_length)
    cheat_lengths = [length - i for i in cheat_lengths]
    cheat_counter = Counter(cheat_lengths)

    best_cheats = 0
    for k, v in cheat_counter.items():
        if k >= 100:
            best_cheats += v
    return length


if __name__ == "__main__":
    input_data = open("input_data.txt").read()
    result = solve(input_data)
    print(f"Example1: {result}")
