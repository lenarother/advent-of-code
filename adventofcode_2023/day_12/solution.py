"""Day 12: Hot Springs

https://adventofcode.com/2023/day/12

"""
import re


def get_regex(counts):
    pattern = r"[.?]*"
    for n in counts:
        pattern += rf"[#?]X{n}Y[.?]+"
    pattern = pattern[:-1] + "*"
    pattern = pattern.replace('X', '{')
    pattern = pattern.replace('Y', '}')
    print(pattern)
    return pattern


def find_arrangement_count(line):
    line_info, counts = line.split(' ')
    counts = [int(i) for i in counts.split(',')]
    template = get_regex(counts)
    print(line)
    # print(re.match(template, line_info))

    ready = set()
    todo = [line_info]
    while todo:
        current = todo.pop()
        if current.count('?') == 0:
            ready.add(current)
        else:
            new_1 = current.replace('?', '.', 1)
            new_2 = current.replace('?', '#', 1)
            if re.match(template, new_1) and new_1.count('#') <= sum(counts):
                todo.append(new_1)
            if re.match(template, new_2) and new_2.count('#') <= sum(counts):
                todo.append(new_2)
    print(ready)
    return len(ready)



    # build regex
    # replace one and add to list
    # get length of list

def unfold_line_info(l):
    return f"{l}?{l}?{l}?{l}?{l}"

def unfold_line_count(c):
    return c + c + c + c + c


def find_arrangement_count_2(line):
    line_info, counts = line.split(' ')
    line_info = unfold_line_info(line_info)
    counts = [int(i) for i in counts.split(',')]
    counts = unfold_line_count(counts)

    template = get_regex(counts)
    print(line)
    print(line_info)
    print(counts)
    # print(re.match(template, line_info))

    ready = set()
    todo = [line_info]
    while todo:
        current = todo.pop()
        if current.count('?') == 0:
            ready.add(current)
        else:
            new_1 = current.replace('?', '.', 1)
            new_2 = current.replace('?', '#', 1)
            if re.match(template, new_1) and new_1.count('#') <= sum(counts):
                todo.append(new_1)
            if re.match(template, new_2) and new_2.count('#') <= sum(counts):
                todo.append(new_2)
    print(ready)
    return len(ready)


def solve(data):
    return sum([find_arrangement_count(line) for line in data.strip().split('\n')])


def solve_2(data):
    return sum([find_arrangement_count_2(line) for line in data.strip().split('\n')])



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    #result = solve(input_data)
    #print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example1: {result}')