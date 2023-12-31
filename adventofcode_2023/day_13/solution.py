"""Day 13: Point of Incidence

https://adventofcode.com/2023/day/13

"""
from collections import defaultdict


def get_rows(data):
    return data.strip().split()


def get_columns(data):
    counter = 0
    d = defaultdict(str)
    for i in data:
        if i == "\n":
            counter = 0
        else:
            d[counter] += i
            counter += 1
    return list(d.values())


def get_vertical_n(columns):
    results = [columns.count(c) for c in columns]
    #print(results)
    #print()

    if results[0] == 1 and results[-1] == 1:
        return 0

    if results[0] == 2:
        return results.count(2) // 2

    else:
        return (results.count(2) // 2) + results.count(1)

def get_horizontal_n(rows):
    a =  100 * get_vertical_n(rows)
    print('---')
    return a

def get_pictures(data):
    return data.strip().split('\n\n')


def solve_bkp(data):
    pictures = get_pictures(data)
    result = 0
    for p in pictures:
        rows = get_rows(p)
        columns = get_columns(p)
        result += get_vertical_n(columns)
        result += get_horizontal_n(rows)
    return result

def rows_from_up(picture):
    # return SIZE of mirror and RESULT (rows up * 100)
    lines = picture.strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[0], range(len(lines))))

    if len(indices) < 2:
        return 0, 0
    for i in reversed(indices):
        candidate = lines[:i + 1]
        if candidate == candidate[::-1]:
            return len(candidate), (len(candidate) // 2) * 100
    return 0, 0


def rows_from_down(picture):
    # return SIZE of mirror and RESULT (rows up * 100)
    lines = picture.strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[-1], range(len(lines))))

    if len(indices) < 2:
        return 0, 0
    for i in indices:
        candidate = lines[i:]
        if candidate == candidate[::-1]:
            return len(candidate), ((len(lines) - len(candidate)) + len(candidate) // 2) * 100
    return 0, 0


def columns_from_left(picture):
    # return SIZE of mirror and RESULT (columns left)
    picture = transpose(picture).strip()
    lines = picture.split('\n')
    indices = list(filter(lambda i: lines[i] == lines[0], range(len(lines))))

    if len(indices) < 2:
        return 0, 0
    for i in reversed(indices):
        candidate = lines[:i + 1]
        if candidate == candidate[::-1]:
            return len(candidate), (len(candidate) // 2)
    return 0, 0

def columns_from_right(picture):
    # return SIZE of mirror and RESULT
    picture = transpose(picture).strip()
    lines = picture.split('\n')
    indices = list(filter(lambda i: lines[i] == lines[-1], range(len(lines))))

    if len(indices) < 2:
        return 0, 0
    for i in indices:
        candidate = lines[i:]
        if candidate == candidate[::-1]:
            return len(candidate), ((len(lines) - len(candidate)) + len(candidate) // 2)
    return 0, 0


def transpose(picture):
    picture = picture.strip().split('\n')
    # print(list(zip(*picture)))
    return '\n'.join(["".join(x) for x in zip(*picture)])

def find_mirror(picture):
    size = 0
    x = 0

    n_size, n_x = rows_from_up(picture)
    if n_size > size:
        size, x = n_size, n_x

    n_size, n_x = rows_from_down(picture)
    if n_size > size:
        size, x = n_size, n_x

    n_size, n_x = columns_from_left(picture)
    if n_size > size:
        size, x = n_size, n_x

    n_size, n_x = columns_from_right(picture)
    if n_size > size:
        size, x = n_size, n_x

    return x


def solve(data):
    result = 0
    for picture in data.split('\n\n'):
        result += find_mirror(picture)
    return result



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
