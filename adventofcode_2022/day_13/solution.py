"""Day 13: Distress Signal

https://adventofcode.com/2022/day/13

"""


def prepare_input(left, right):
    if isinstance(left, str):
        left = eval(left)
    if isinstance(right, str):
        right = eval(right)
    if type(left) == type(right):
        return left, right
    if isinstance(left, int):
        return [left], right
    return left, [right]


def compare_digits(left, right):
    if left == right:
        return None
    return left < right


def compare_lists(left, right):
    left, right = prepare_input(left, right)
    result = None
    for l, r in zip(left, right):
        l, r = prepare_input(l, r)
        if isinstance(l, int):
            result = compare_digits(l, r)
            if result is not None:
                return result
        if isinstance(l, list):
            result = compare_lists(l, r)
            if result is not None:
                return result
    if len(left) == len(right):
        return None
    return len(left) < len(right)


def items(data):
    for i in data.strip().split('\n\n'):
        yield i.split('\n')


def solve(data):
    n = 1
    result = 0
    for l, r in items(data):
        result += compare_lists(l, r) * n
        n += 1
    return result

    # return True
    # return sum([compare_lists(l, r) for l, r in items(data)])


# def compare_pair(left, right):


# Python program for implementation of Quicksort Sort

# This implementation utilizes pivot as the last element in the nums list
# It has a pointer to keep track of the elements smaller than the pivot
# At the very end of partition() function, the pointer is swapped with the pivot
# to come up with a "sorted" nums relative to the pivot

class Item:

    def __init__(self, str_repr):
        self.str_repr = str_repr

    def __eq__(self, other):
        return self.str_repr == other.str_repr

    def __lt__(self, other):
        return compare_lists(self.str_repr, other.str_repr)


def solve2(data):
    first = Item('[[2]]')
    second = Item('[[6]]')
    to_sort = [first, second]
    for l, r in items(data):
        to_sort.append(Item(l))
        to_sort.append(Item(r))
    to_sort.sort()
    x = to_sort.index(first)
    y = to_sort.index(second)
    return (x + 1) * (y + 1)



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')

"""If both values are integers, the lower integer should come first. If the left integer is lower than the right integer, the inputs are in the right order. If the left integer is higher than the right integer, the inputs are not in the right order. Otherwise, the inputs are the same integer; continue checking the next part of the input.
If both values are lists, compare the first value of each list, then the second value, and so on. If the left list runs out of items first, the inputs are in the right order. If the right list runs out of items first, the inputs are not in the right order. If the lists are the same length and no comparison makes a decision about the order, continue checking the next part of the input.
If exactly one value is an integer, convert the integer to a list which contains that integer as its only value, then retry the comparison. For example, if comparing [0,0,0] and 2, convert the right value to [2] (a list containing 2); the result is then found by instead comparing [0,0,0] and [2].
Using these rules, you can determine which of the pairs in the example are in the right order:

== Pair 1 ==
- Compare [1,1,3,1,1] vs [1,1,5,1,1]
  - Compare 1 vs 1
  - Compare 1 vs 1
  - Compare 3 vs 5
    - Left side is smaller, so inputs are in the right order

== Pair 2 ==
- Compare [[1],[2,3,4]] vs [[1],4]
  - Compare [1] vs [1]
    - Compare 1 vs 1
  - Compare [2,3,4] vs 4
    - Mixed types; convert right to [4] and retry comparison
    - Compare [2,3,4] vs [4]
      - Compare 2 vs 4
        - Left side is smaller, so inputs are in the right order

== Pair 3 ==
- Compare [9] vs [[8,7,6]]
  - Compare 9 vs [8,7,6]
    - Mixed types; convert left to [9] and retry comparison
    - Compare [9] vs [8,7,6]
      - Compare 9 vs 8
        - Right side is smaller, so inputs are not in the right order

== Pair 4 ==
- Compare [[4,4],4,4] vs [[4,4],4,4,4]
  - Compare [4,4] vs [4,4]
    - Compare 4 vs 4
    - Compare 4 vs 4
  - Compare 4 vs 4
  - Compare 4 vs 4
  - Left side ran out of items, so inputs are in the right order

== Pair 5 ==
- Compare [7,7,7,7] vs [7,7,7]
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Compare 7 vs 7
  - Right side ran out of items, so inputs are not in the right order

== Pair 6 ==
- Compare [] vs [3]
  - Left side ran out of items, so inputs are in the right order

== Pair 7 ==
- Compare [[[]]] vs [[]]
  - Compare [[]] vs []
    - Right side ran out of items, so inputs are not in the right order

== Pair 8 ==
- Compare [1,[2,[3,[4,[5,6,7]]]],8,9] vs [1,[2,[3,[4,[5,6,0]]]],8,9]
  - Compare 1 vs 1
  - Compare [2,[3,[4,[5,6,7]]]] vs [2,[3,[4,[5,6,0]]]]
    - Compare 2 vs 2
    - Compare [3,[4,[5,6,7]]] vs [3,[4,[5,6,0]]]
      - Compare 3 vs 3
      - Compare [4,[5,6,7]] vs [4,[5,6,0]]
        - Compare 4 vs 4
        - Compare [5,6,7] vs [5,6,0]
          - Compare 5 vs 5
          - Compare 6 vs 6
          - Compare 7 vs 0
            - Right side is smaller, so inputs are not in the right order
"""