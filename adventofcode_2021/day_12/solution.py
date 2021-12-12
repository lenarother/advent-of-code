"""Day 12: Passage Pathing

https://adventofcode.com/2021/day/12

"""
from collections import Counter, defaultdict, deque


class Cave:
    def __init__(self, data=None):
        self.moves = self.parse(data) if data else {}

    @staticmethod
    def parse(data):
        move_map = defaultdict(set)
        for line in data.strip().split('\n'):
            n1, n2 = line.split('-')
            if n1 != 'end' and n2 != 'start':
                move_map[n1].add(n2)
            if n2 != 'end' and n1 != 'start':
                move_map[n2].add(n1)
        return move_map

    @staticmethod
    def has_no_lowercase_duplicates(node, path):
        if node.isupper():
            return True
        if node not in path:
            return True
        return False

    def has_at_most_one_lowercase_duplicate(self, node, path):
        if self.has_no_lowercase_duplicates(node, path):
            return True
        return not any([
            node.islower() and count > 1
            for node, count in Counter(path).items()
        ])

    def find_paths(self, condition):
        ready = []
        paths = deque([['start']])

        while paths:
            path = paths.popleft()
            last_node = path[-1]
            if last_node == 'end':
                ready.append(path)
                continue
            for new_node in self.moves[last_node]:
                if condition(new_node, path):
                    paths.append(path + [new_node])

        return ready

    def count_paths(self, mode='no_duplicates'):
        algorithms = {
            'no_duplicates': self.has_no_lowercase_duplicates,
            'single_duplicate': self.has_at_most_one_lowercase_duplicate,
        }
        paths = self.find_paths(algorithms[mode])
        return len(paths)


def solve(data, mode='no_duplicates'):
    c = Cave(data)
    return c.count_paths(mode)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, mode='no_duplicates')
    print(f'Example1: {result}')

    result = solve(input_data, mode='single_duplicate')
    print(f'Example2: {result}')
