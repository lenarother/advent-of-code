"""Day 17: Pyroclastic Flow

https://adventofcode.com/2022/day/17

The first rock begins falling:
|..@@@@.|
|.......|
|.......|
|.......|
+-------+

Jet of gas pushes rock right:
|...@@@@|
|.......|
|.......|
|.......|
+-------+

Rock falls 1 unit:
|...@@@@|
|.......|
|.......|
+-------+


..@@@@.|
|.......|
|.......|
|.......|
|....##.|
|....##.|
|....#..|
|..#.#..|
|..#.#..|
|#####..|
|..###..|
|...#...|
|..####.|
+-------+
"""
from itertools import cycle


# 0, 7
SHAPES = {
    #  ####
    1: [(2, 0), (3, 0), (4, 0), (5, 0)],

    #  .#.
    #  ###
    #  .#.
    2: [(3, 0), (2, 1), (3, 1), (4, 1), (3, 2)],

    #  ..#
    #  ..#
    #  ###
    3: [(2, 0), (3, 0), (4, 0), (4, 1), (4, 2)],

    #  #
    #  #
    #  #
    #  #
    4: [(2, 0), (2, 1), (2, 2), (2, 3)],

    #  ##
    #  ##
    5: [(2, 0), (3, 0), (2, 1), (3, 1)],
}

HEIGHTS = {
    1: 1,
    2: 3,
    3: 3,
    4: 4,
    5: 2,

}


def pieces(SHAPES):
    for shape in cycle(SHAPES.values()):
        yield shape


def directions(moves):
    for move in cycle(moves):
        yield move


def shift(shape, move):
    if move == '>':
        return [(x + 1, y) for x, y in shape]
    elif move == '<':
        return [(x - 1, y) for x, y in shape]


def fall(shape):
    return [(x, y - 1) for x, y in shape]


def is_possible(shape, space):
    # Other rock
    if any([i in space for i in shape]):
        return False

    # Wall
    if not all(0 <= i[0] < 7 for i in shape):
        return False

    # Flor
    if not all(i[1] >= 0 for i in shape):
        return False

    return True


def get_new_piece(current_max_height, shape):
    return [(i[0], (i[1] + current_max_height + 3)) for i in shape]


def one_turn(shape, move, space):
    bkp = [i for i in shape]
    candidate = shift(shape, move)
    if is_possible(candidate, space):
        shape = candidate
        can_shift = True
    else:
        shape = bkp
        can_shift = False

    bkp = [i for i in shape]
    candidate = fall(shape)
    if is_possible(candidate, space):
        shape = candidate
        can_fall = True
    else:
        shape = bkp
        can_fall = False

    return shape, can_shift, can_fall


def solve(data, n):
    space = set()
    current_max_height = 0

    piece = pieces(SHAPES)
    direction = directions(data)

    while n:
        n -= 1
        current_shape = get_new_piece(current_max_height, next(piece))
        #print(current_shape)
        #draw_space(space | set(current_shape))

        can_fall = True

        while can_fall:
            current_direction = next(direction)
            #print(current_direction)
            current_shape, can_shift, can_fall = one_turn(current_shape, current_direction, space)
            #draw_space(space | set(current_shape))
            #print('---------')
        space |= set(current_shape)
        current_max_height = max(current_max_height, max([i[1] for i in current_shape]) + 1)
        #print(current_max_height)
        draw_space(space)
        #print('-' * 20)
    return current_max_height


def draw_space(space):
    repr = '\n'
    for y in range(100, -1, -1):
        for x in range(7):
            p = (x, y)
            repr += '#' if p in space else '.'
        repr += '\n'
    print(repr)
    return repr


if __name__ == '__main__':
    input_data = open('input_data.txt').read().strip()
    result = solve(input_data, 2022)
    print(f'Example1: {result}')
