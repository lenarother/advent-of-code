"""Day 16: Proboscidea Volcanium

https://adventofcode.com/2022/day/16

"""
import re
PATTERN = re.compile(r'Valve ([A-Z]+) has flow rate=(\d+); tunnels? leads? to valves? ([A-Z,\s]+)\n')


def parse(data):
    values = {}
    connections = {}
    for valve, value, connected in PATTERN.findall(data):
        values[valve] = int(value)
        connections[valve] = connected.split(', ')
    return values, connections


def paths(connections):
    todo = [['AA']]
    while todo:
        print(todo)
        new_todo = []
        for i in todo:
            print(i)
            for j in connections[i[-1]]:
                print(j)
                if j in i:
                    print(i)
                    yield i
                else:
                    i.append(j)
                    new_todo.append(i)
        todo = new_todo


def open_valve(valve, values, t ):
    return values[valve] * t-1


def paths_value(p, values, trashold=0):
    foo = 0
    t = 30
    i = 0
    while t and i < len(p):
        valve = p[i]
        value = values[valve]
        t -= 1
        if value > trashold:
            foo += values[valve] * t
            t -= 1
        i += 1
    return foo


def calc_best_path_value(p, values):
    print(p)
    aaa = []
    for trashold in range(30):
        aaa.append(paths_value(p, values, trashold))
    best = max(aaa)
    return best


def solve(data):
    results = []
    values, connections = parse(data)
    for p in paths(connections):
        results.append(calc_best_path_value(p, values))
    return max(results)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
