"""Day 12: Digital Plumber

https://adventofcode.com/2017/day/12

"""


def parse(data):
    ids = {}
    for line in data.strip().split('\n'):
        k, v = line.strip().split(' <-> ')
        ids[int(k)] = set(map(int, v.split(', ')))
    return ids


def find_group(ids, group):
    look_for = {group} | ids[group]
    changed = True

    while changed:
        new_ids = set()
        for k, v in ids.items():
            if k not in look_for:
                if look_for.intersection(v):
                    new_ids.add(k)
        if not new_ids:
            changed = False
        look_for |= new_ids

    return look_for


def solve(data, group=0):
    ids = parse(data)
    return len(find_group(ids, group))


def solve2(data):
    ids = parse(data)
    groups_count = 0

    while ids:
        k = list(ids.keys())[0]
        group = find_group(ids, k)
        for i in group:
            ids.pop(i)
        groups_count += 1

    return groups_count


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example1: {result}')
