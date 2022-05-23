"""Day 7: Recursive Circus

https://adventofcode.com/2017/day/7

"""
import re

RELATION = re.compile(r'(\w+) \(\d+\) -> (.*)')
WEIGHT_PARENT = re.compile(r'(\w+) \((\d+)\) ->')
WEIGHT_LEAF = re.compile(r'(\w+) \((\d+)\)\n')


def parse_relations(data):
    return {
        k: set(v.split(', '))
        for k, v in RELATION.findall(data)
    }


def parse_weight(data, expression=WEIGHT_LEAF):
    return {
        k: int(v)
        for k, v in expression.findall(data)
    }


def solve(data):
    relations = parse_relations(data)
    result = set(relations.keys()) - set().union(*relations.values())
    return result.pop()


def find_correct_weight(names, ready_weights, todo_weights):
    incorrect_weight = 0
    correct_weight = 0
    names = list(names)
    weights = [ready_weights[n] for n in names]

    for n, w in zip(names, weights):
        if weights.count(w) == 1:
            incorrect_weight = w
            name = n
        else:
            correct_weight = w

    d = correct_weight - incorrect_weight
    orig_weight = todo_weights.get(name, None) or ready_weights.get(name)
    return orig_weight + d


def solve2(data):
    ready_weights = parse_weight(data)
    todo_weights = parse_weight(data, WEIGHT_PARENT)
    relations = parse_relations(data)

    while 1:

        for name, children in relations.items():
            children_weights = [ready_weights.get(ch, None) for ch in children]
            if name not in ready_weights and all(children_weights):
                if len(set(children_weights)) == 1:
                    ready_weights[name] = (
                        sum(children_weights) +
                        todo_weights[name]
                    )
                else:
                    return find_correct_weight(
                        children,
                        ready_weights,
                        todo_weights
                    )


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
