"""Day 17: Clumsy Crucible

https://adventofcode.com/2023/day/17

"""
import heapq

from santa_helpers import parse_grid_to_dict
from santa_helpers.neighbors import NEIGHBORS_N, is_point_in_range


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
        point, direction
        (x, y), (dx, dy)
    """
    neighbor_points = NEIGHBORS_N[n]
    x, y = p
    for dx, dy in neighbor_points:
        new_p = (x + dx, y + dy)
        if is_point_in_range(new_p, p_min, p_max):
            yield new_p, (dx, dy)


def dijkstra(data, max_moves=3, min_moves=0):
    costs = parse_data(data)
    max_x = column_count(data) - 1
    max_y = row_count(data) - 1
    target = (max_x, max_y)
    visited = set()

    # priority queue
    h = []
    heapq.heappush(h, (0, (0, 0), (0, 0), 0))

    while h:
        current_cost, current_position, past_direction, n_past_moves = (
            heapq.heappop(h)
        )
        if current_position == target and n_past_moves >= min_moves:
            return current_cost

        neighbors_gen = neighbors(
            current_position,
            p_min=(0, 0),
            p_max=target,
        )
        for neighbor, direction in neighbors_gen:
            new_n_past_moves = (
                n_past_moves + 1 if direction == past_direction else 1
            )

            # Invalid cases:
            # Only allowed to go max_moves forward (than have to turn)
            if new_n_past_moves > max_moves:
                continue
            # Don't go if already visited
            if (neighbor, direction, new_n_past_moves) in visited:
                continue
            # Going back is not allowed
            if (
                direction != past_direction and
                (
                    (abs(direction[0]), abs(direction[1])) ==
                    (abs(past_direction[0]), abs(past_direction[1]))
                )
            ):
                continue
            # Must go min_moves steps in straight line
            if (
                past_direction != (0, 0) and  # starting point has no direction
                direction != past_direction and
                n_past_moves < min_moves
            ):
                continue

            # Valid point
            visited.add((neighbor, direction, new_n_past_moves))
            new_cost = current_cost + costs[neighbor]
            heapq.heappush(
                h,
                (new_cost, neighbor, direction, new_n_past_moves)
            )


def solve(data):
    return dijkstra(data)


def solve_2(data):
    return dijkstra(data, max_moves=10, min_moves=4)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
