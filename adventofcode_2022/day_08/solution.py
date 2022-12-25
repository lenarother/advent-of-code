"""Day 8: Treetop Tree House

https://adventofcode.com/2022/day/8

"""


def parse(data: str) -> dict:
    return {
        (x, y): v
        for y, row in enumerate(data.strip().split('\n'))
        for x, v in enumerate(row.strip())
    }


def get_row_length(data):
    return len(data.strip().split('\n')[0])


def get_column_length(data):
    return len(data.strip().split('\n'))


def get_all_negbour(tree, data, direction, raw_data):
    row_length = get_row_length(raw_data)
    column_length = get_column_length(raw_data)
    x, y = tree
    trees = []
    if direction == 'R':
        for n in range(x+1, row_length):
            trees.append(data[n, y])
    if direction == 'L':
        for n in range(0, x):
            trees.append(data[n, y])
    if direction == 'D':
        for n in range(y+1, column_length):
            trees.append(data[x, n])
    if direction == 'U':
        for n in range(0, y):
            trees.append(data[x, n])
    return trees


def neighbours(tree, data, direction, raw_data):
    row_length = get_row_length(raw_data)
    column_length = get_column_length(raw_data)
    x, y = tree
    trees = []
    if direction == 'R':
        # print(direction, tree, x+1, row_length)
        for n in range(x+1, row_length):
            if data[n, y] < data[tree]:
                yield data[n, y]
            else:
                yield data[n, y]
                return
    if direction == 'L':
        # print(direction, tree, 0, x)
        for n in reversed(range(0, x)):
            # yield data[n, y]
            if data[n, y] < data[tree]:
                yield data[n, y]
            else:
                yield data[n, y]
                return
    if direction == 'D':
        # print(direction, tree, y + 1, column_length) (2, 2)
        for n in range(y+1, column_length):
            # yield data[x, n]
            if data[x, n] < data[tree]:
                yield data[x, n]
            else:
                yield data[x, n]
                return
    if direction == 'U':
        # print(direction, tree, 0, y)
        for n in reversed(range(0, y)):
            # yield data[x, n]
            if data[x, n] < data[tree]:
                yield data[x, n]
            else:
                yield data[x, n]
                return
    #return trees


def is_visible(tree, data, raw_data):
    x, y = tree
    row_length = get_row_length(raw_data)
    column_length = get_column_length(raw_data)
    if x == 0 or y == 0:
        return True
    if x == row_length - 1:
        return True
    if y == column_length - 1:
        return True

    for direction in 'LRUD':
        neigbours = get_all_negbour(tree, data, direction, raw_data)
        if max(neigbours) < data[tree]:
            return True
    return False


def get_score(tree, data, raw_data):
    x, y = tree
    row_length = get_row_length(raw_data)
    column_length = get_column_length(raw_data)
    if x == 0 or y == 0:
        return 0
    elif x == row_length - 1:
        return 0
    elif y == column_length - 1:
        return 0

    # score = 0
    foo = []
    print(tree)
    for direction in 'LRUD':
        print(list(neighbours(tree, data, direction, raw_data)))
        foo.append(len(list(neighbours(tree, data, direction, raw_data))))
    print(foo)
    print('SCORE', foo[0] * foo[1] * foo[2] * foo[3])
    print('----------------------')
    return foo[0] * foo[1] * foo[2] * foo[3]

def solve(data):
    visible = 0
    trees = parse(data)
    for tree in trees:
        if is_visible(tree, trees, data):
            visible += 1
    return visible

def solve2(data):
    visible = 0
    trees = parse(data)
    scores = []
    for tree in trees:
        score = get_score(tree, trees, data)
        scores.append(score)
    return max(scores)

if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')