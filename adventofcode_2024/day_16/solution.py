"""Day 16: Reindeer Maze

https://adventofcode.com/2024/day/16

"""
from copy import copy
import heapq

NEIGHBORS = [
                 ((0, -1), 'N'),               # noqa N
    ((-1, 0), 'W'),            ((1, 0), 'E'),  # noqa W E
                 ((0,  1), 'S'),               # noqa S
]

DIRECTIONS = 'NWSE'


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
        elif DIRECTIONS.index(direction) % 2 == DIRECTIONS.index(new_direction) % 2:
            cost = 2001
        else:
            cost = 1001
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

    visited_nodes = set()
    unvisited_nodes = []
    heapq.heappush(unvisited_nodes, (0, (start, direction)))

    while unvisited_nodes:
        price, current_node = heapq.heappop(unvisited_nodes)
        position, direction = current_node
        if position == end:
            return price
        if position not in visited_nodes:
            visited_nodes.add(position)
            for neighbor, new_direction, cost in neighbors(position, direction):
                if grid[neighbor] in '.E':
                    new_price = price + cost
                    heapq.heappush(unvisited_nodes, (new_price, (neighbor, new_direction)))


# def solve2(data):
#     import heapq
#
#     grid = get_grid_dict(data)
#     start = get_position(grid, 'S')
#     end = get_position(grid, 'E')
#     direction = 'E'
#
#     visited_nodes = set()
#     unvisited_nodes = []
#     for i in grid:
#         if i == start:
#             heapq.heappush(unvisited_nodes, (0, (i, direction)))
#         else:
#             heapq.heappush(unvisited_nodes, (1000_1000_1000, (i, None)))
#
#     distance_table = {k: 1000_1000_1000 for k in grid if k != '#'}
#     #distance_table[start] = 0
#     #previous_node = {k: None for k in grid if k != '#'}
#
#     while unvisited_nodes:
#         price, current_node = heapq.heappop(unvisited_nodes)
#         position, direction = current_node
#         if position == end:
#             return price
#         if position not in visited_nodes:
#             visited_nodes.add(position)
#             for neighbor, new_direction, cost in neighbors(position, direction):
#                 if grid[neighbor] in '.E':
#                     new_price = price + cost
#                     heapq.heappush(unvisited_nodes, (new_price, (neighbor, new_direction)))
#

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
