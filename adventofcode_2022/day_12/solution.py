"""Day 12: Hill Climbing Algorithm

https://adventofcode.com/2022/day/12

"""
from string import ascii_lowercase

LETTERS = list(ascii_lowercase)
MOVES = [(0, 1), (0, -1), (1, 0), (-1, 0)]


def parse(data: str) -> dict:
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def get_position_of_value(value, maze):
    positions = []
    for p, v in maze.items():
        if v == value:
            positions.append(p)
    return positions


def neighbors(p):
    x, y = p
    for dx, dy in MOVES:
        yield x + dx, y + dy


def get_height(position, maze):
    height = maze[position]
    return 'a' if height == 'S' else 'z' if height == 'E' else height


def is_possible(move, maze, current_height):
    if move not in maze:
        return False
    next_height = get_height(move, maze)
    if current_height >= next_height:
        return True
    return LETTERS.index(current_height) + 1 == LETTERS.index(next_height)


def sol(maze, start_positions):
    end_position = get_position_of_value('E', maze)[0]

    for start_position in start_positions:
        positions = {start_position}
        visited = set()
        counter = 0
        while end_position not in positions and counter <= 500:
            new_positions = set()
            while positions:
                p = positions.pop()
                p_value = get_height(p, maze)
                visited.add(p)
                for i in neighbors(p):
                    if i not in visited and is_possible(i, maze, p_value):
                        new_positions.add(i)
            positions = new_positions
            counter += 1
        yield counter


def solve(data):
    maze = parse(data)
    start_position = get_position_of_value('S', maze)
    return min(sol(maze, start_positions=start_position))


def solve2(data):
    maze = parse(data)
    start_position = get_position_of_value('a', maze)
    return min(sol(maze, start_positions=start_position))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
