"""Day 21: Monkey Math

https://adventofcode.com/2022/day/21

"""
import re

RE_MONKEY = re.compile(r'(\w+): ([a-zA-Z0-9]+)\s?([\+\-\*\/])?\s?(\w+)?\n')


def parse(data):
    ready = {}
    todo = {}

    for m in RE_MONKEY.findall(data):
        if m[1].isdigit():
            ready[m[0]] = int(m[1])
        else:
            todo[m[0]] = [m[1], m[2], m[3]]
    return ready, todo


def solve(data):
    ready, todo = parse(data)

    while todo:
        to_remove = []
        for k, v in todo.items():
            if v[0] in ready and v[2] in ready:
                ready[k] = eval(f'{ready[v[0]]} {v[1]} {ready[v[2]]}')
                to_remove.append(k)

        for k in to_remove:
            todo.pop(k)

    return ready['root']


def solve2(data):
    ready, todo = parse(data)
    ready.pop('humn')
    root = todo.pop('root')


    while todo:
        to_remove = []
        for k, v in todo.items():
            if k == 'root':
                if v[0] in ready:
                    ready[v[1]] = v[0]
                    ready['humn'] = v[0]
                    to_remove.append([v[1]])
                    to_remove.append('root')

                elif v[1] in ready:
                    ready[v[0]] = v[1]
                    ready['humn'] = v[1]
                    to_remove.append([v[0]])

                    to_remove.append('root')

            elif v[0] in ready and v[2] in ready:
                ready[k] = eval(f'{ready[v[0]]} {v[1]} {ready[v[2]]}')
                to_remove.append(k)
        if not to_remove:
           break

        for k in to_remove:
            try:
                todo.pop(k)
            except KeyError:
                pass
    import pprint
    pprint.pprint(ready)
    pprint.pprint(todo)

    return ready['humn']


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    # result = solve2(input_data)