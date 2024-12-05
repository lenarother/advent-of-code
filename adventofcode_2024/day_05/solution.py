"""Day 5: Print Queue

https://adventofcode.com/2024/day/5

"""
from collections import defaultdict


def get_rules(data):
    """
    Parse rules (first part of the input data) to a dict.

    1 | 5
    1 | 6
    2 | 7

    Returns
        {1: {5, 6}, 2: {7}}
        Both keys and elements are strings.
    """
    data = data.strip().split('\n\n')[0]
    rules = defaultdict(set)
    for i in data.strip().split('\n'):
        x, y = i.split('|')
        rules[x].add(y)
    return rules


def get_updates(data):
    """Parse updates (second part of the input data) to a list of lists"""
    data = data.strip().split('\n\n')[1]
    return [i.split(',') for i in data.strip().split('\n')]


def check_update(update, rules, is_correct=True):
    """Return update if check is positive, otherwise None

    Check for correct or incorrect updates,
    depending on is_correct input value.
    """
    to_check = update.copy()
    for _ in range(len(to_check) - 1):
        first = to_check.pop(0)
        if len(set(to_check) - rules[first]) != 0:
            return None if is_correct else update
    return update if is_correct else None


def get_sum_of_middle_pages(updates):
    """Return sum of list middle elements from list of lists

    Outer list may contain inner lists or None elements.
    """
    return sum([int(i[len(i) // 2]) for i in filter(None, updates)])


def solve(data):
    rules = get_rules(data)
    updates = get_updates(data)
    sorted_updates = [check_update(update, rules) for update in updates]
    return get_sum_of_middle_pages(sorted_updates)


def order_update(update, rules):
    ordered_update = []
    while update:
        for i in update:
            temp = update.copy()
            temp.remove(i)
            if len(set(temp) - rules[i]) == 0:
                ordered_update.append(i)
                update.remove(i)
                continue
    return ordered_update


def solve2(data):
    rules = get_rules(data)
    updates = get_updates(data)
    incorrect_updates = [
        check_update(update, rules, is_correct=False)
        for update in updates
    ]
    sorted_updates = [
        order_update(i, rules)
        for i in filter(None, incorrect_updates)
    ]
    return get_sum_of_middle_pages(sorted_updates)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
