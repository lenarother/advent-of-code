"""Day 17: Clumsy Crucible

https://adventofcode.com/2023/day/17

"""
import heapq
from santa_helpers import parse_grid_to_dict, neighbors
from santa_helpers.neighbors import is_point_in_range, NEIGHBORS_N


def column_count(data: str) -> int:
    return len(data.strip().split('\n')[0])


def row_count(data: str) -> int:
    return int(
        len(data.strip().replace('\n', '')) /
        len(data.strip().split('\n')[0])
    )


def parse_data(data):
    data = parse_grid_to_dict(data.strip())
    return {k: int(v) for k, v in data.items()}


def neighbors(p, n=4, p_min=None, p_max=None):
    """Point neighbor generator.

    Args:
        p: tuple (x, y)
        n: int 4 (no diagonal) or 8 (with diagonal)
        p_min (optional): min grid point, if not given infinite
        p_max (optional): max grid point, if not given infinite

    Yields:
        point (x, y)
    """
    neighbor_points = NEIGHBORS_N[n]
    x, y = p
    for dx, dy in neighbor_points:
        new_p = (x + dx, y + dy)
        if is_point_in_range(new_p, p_min, p_max):
            yield new_p, (dx, dy)


def solve(data):
    costs = parse_data(data)
    max_x = column_count(data) - 1
    max_y = row_count(data) - 1
    target = (max_x, max_y)
    # print(costs)
    visited = set()
    h = []
    heapq.heappush(h, (0, (0, 0), (0, 0), 0))
    while h:
        current_cost, current_position, past_direction, n_past_moves = heapq.heappop(h)
        if current_position == target:  
            return current_cost

        neighbors_gen = neighbors(
            current_position,
            p_min=(0, 0),
            p_max=target,
        )
        for neighbor, direction in neighbors_gen:
            if direction != past_direction:
                new_n_past_moves = 1
            else:
                new_n_past_moves = n_past_moves + 1

            if new_n_past_moves > 3:
                continue
            if (neighbor, direction, new_n_past_moves) in visited:
                continue
            if direction != past_direction and (abs(direction[0]), abs(direction[1])) == (abs(past_direction[0]), abs(past_direction[1])):
                continue

            visited.add((neighbor, direction, new_n_past_moves))
            new_cost = current_cost + costs[neighbor]
            heapq.heappush(h, (new_cost, neighbor, direction, new_n_past_moves))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
