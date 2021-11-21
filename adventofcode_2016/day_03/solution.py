"""Day 3: Squares With Three Sides

https://adventofcode.com/2016/day/3

In a valid triangle, the sum of any two sides
must be larger than the remaining side. For example,
the "triangle" given above is impossible,
because 5 + 10 is not larger than 25.

In your puzzle input, how many of the listed triangles are possible?
"""


def is_triangle_valid(edges):
    a, b, c = sorted(edges)
    if a + b > c:
        return True
    return False


def count_valid_triangles(triangles_list):
    return sum(map(is_triangle_valid, triangles_list))


def read_input(f):
    return [map(int, line.strip().split()) for line in f]


def read_input_vertically(f):
    data = list(read_input(f))
    for i in range(0, len(data), 3):
        temp = [data[i], data[i+1], data[i+2]]
        for result in zip(*temp):
            yield result


if __name__ == '__main__':
    input_data = read_input(open('input_data.txt'))
    print(f'Example1: {count_valid_triangles(input_data)}')

    input_data = read_input_vertically(open('input_data.txt'))
    print(f'Example2: {count_valid_triangles(input_data)}')
