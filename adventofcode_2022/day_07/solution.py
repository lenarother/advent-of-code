"""Day 7: No Space Left On Device

https://adventofcode.com/2022/day/7

"""
from __future__ import annotations

from dataclasses import dataclass


@dataclass
class AocData:
    name: str
    size: int | None = None
    children: dict | None = None
    parent: AocData | None = None

    @property
    def is_dir(self):
        return not self.size or self.children

    def __repr__(self):
        return (
            f'<{"Dir" if self.is_dir else "File"}: {self.name} | {self.size}>'
        )


def handle_cd(command, current_dir, root):
    """No adding new roots"""
    destination = command.split()[1]
    if destination == '/':
        return root
    elif destination == '..':
        return current_dir.parent
    else:
        return current_dir.children[destination]


def handle_ls(command, current_dir, all_nodes):
    if current_dir.children is None:
        current_dir.children = {}
    children = command.split('\n')[1:]
    for ch in children:
        ch_type, name = ch.split()
        new_node = AocData(name=name, parent=current_dir)
        if ch_type == 'dir':
            new_node.children = {}
        if ch_type.isdigit():
            new_node.size = int(ch_type)
        current_dir.children[name] = new_node

        if new_node.is_dir:
            all_nodes.append(new_node)


def parse(data):
    root = AocData(name='.', children={})
    current_dir = root
    all_nodes = [root]

    data = data.strip()
    for command in data.split('$ '):
        command = command.strip()
        if command.startswith('cd'):
            current_dir = handle_cd(command, current_dir, root)
        elif command.startswith('ls'):
            handle_ls(command, current_dir, all_nodes)
    return root, all_nodes


def calculate_size(node):
    if node.size:
        return node.size
    ch_size = 0
    for ch in node.children.values():
        if ch.is_dir and not ch.size:
            ch_size += calculate_size(ch)
        else:
            ch_size += ch.size
    node.size = ch_size
    return node.size


def traverse(node):
    for n in node.children.values():
        if n.is_dir:
            for subn in traverse(n):
                yield subn
    yield node


def solve(data):
    root, all_nodes = parse(data)
    calculate_size(root)
    return sum([n.size for n in traverse(root) if n.size <= 100000])


def solve2(data):
    root, all_nodes = parse(data)
    calculate_size(root)
    space_needed = 30000000 - (70000000 - root.size)
    return min([n.size for n in traverse(root) if n.size >= space_needed])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
