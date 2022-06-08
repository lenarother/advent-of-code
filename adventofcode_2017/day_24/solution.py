"""Day 24: Electromagnetic Moat

https://adventofcode.com/2017/day/24

"""
from collections import defaultdict


def parse(data):
    components = defaultdict(set)

    data = data.strip()
    if data:
        for line in data.strip().split('\n'):
            a, b = list(map(int, line.split('/')))
            components[a].add((a, b))
            components[b].add((a, b))

    return components


def calculate_strength(bridge):
    _, components, strength = bridge
    return strength or sum(sum(port) for port in components)


def get_valid_components(bridge, components):
    """Get possible next components as a list."""
    port, current_components, _ = bridge
    return [
        c for c in components.get(port, [])
        if c not in current_components
    ]


def get_extended_bridge(bridge, component):
    current_port, current_elements, _ = bridge
    port1, port2 = component
    port = port2 if port1 == current_port else port1
    elements = list(current_elements)
    elements.append(component)
    return port, frozenset(elements), 0


def get_stronger_bridge(best_bridge, bridge):
    best_bridge_strength = calculate_strength(best_bridge)
    bridge_strength = calculate_strength(bridge)
    bridge = (bridge[0], bridge[1], bridge_strength)
    return bridge if bridge_strength > best_bridge_strength else best_bridge


def get_longer_bridge(best_bridge, bridge):
    best_bridge_length = len(best_bridge[1])
    bridge_length = len(bridge[1])
    if bridge_length == best_bridge_length:
        return get_stronger_bridge(best_bridge, bridge)
    return bridge if bridge_length > best_bridge_length else best_bridge


def solve(data, get_better_bridge=get_stronger_bridge):
    components = (parse(data))
    bridges = set()
    best_bridge = (0, frozenset(), 0)  # port, components, strength
    bridges.add(best_bridge)

    while bridges:
        bridge = bridges.pop()
        valid_components = get_valid_components(bridge, components)
        for component in valid_components:
            bridges.add(get_extended_bridge(bridge, component))
        if not valid_components:
            best_bridge = get_better_bridge(best_bridge, bridge)

    return calculate_strength(best_bridge)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve(input_data, get_longer_bridge)
    print(f'Example2: {result}')
