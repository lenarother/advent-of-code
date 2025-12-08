"""Day 8: Playground

https://adventofcode.com/2025/day/8

"""
import math


def get_distance(box1, box2):
    x1, y1, z1 = box1
    x2, y2, z2 = box2
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2 + (z1 - z2) ** 2)


def parse_data(data):
    data_dict = {}
    for box in data.strip().split('\n'):
        data_dict[box] = tuple(int(i) for i in box.split(','))
    return data_dict


def calculate_distances(data_dict):
    distance_dict = {}
    for box1 in data_dict:
        for box2 in data_dict:
            k = ' - '.join(sorted([box1, box2]))
            if box1 != box2 and k not in distance_dict:
                distance = get_distance(data_dict[box1], data_dict[box2])
                distance_dict[k] = distance
    return distance_dict


def connect(sorted_pairs, n=10):
    circuits = []
    while n:
        n -= 1
        box_pair = sorted_pairs.pop(0)[0]
        box1, box2 = box_pair.split(' - ')
        overlaps = []
        for i, circuit in enumerate(circuits.copy()):
            if box1 in circuit or box2 in circuit:
                overlaps.append(circuit)
        if overlaps:
            for o in overlaps:
                circuits.remove(o)
            overlaps.append({box1, box2})
            new_circuit = set().union(*overlaps)
            circuits.append(new_circuit)
        else:
            circuits.append({box1, box2})
    return circuits


def connect2(sorted_pairs, all_boxes_count):
    circuits = []
    while sorted_pairs:
        box_pair = sorted_pairs.pop(0)[0]
        box1, box2 = box_pair.split(' - ')
        overlaps = []
        for i, circuit in enumerate(circuits.copy()):
            if box1 in circuit or box2 in circuit:
                overlaps.append(circuit)
        if overlaps:
            for o in overlaps:
                circuits.remove(o)
            overlaps.append({box1, box2})
            new_circuit = set().union(*overlaps)
            circuits.append(new_circuit)
            if len(new_circuit) == all_boxes_count:
                x1, _, _ = box1.split(',')
                x2, _, _ = box2.split(',')
                return int(x1) * int(x2)
        else:
            circuits.append({box1, box2})
    return circuits


def solve(data, n=10):
    data_dict = parse_data(data)
    distance_dict = calculate_distances(data_dict)
    sorted_pairs = sorted(distance_dict.items(), key=lambda item: item[1])
    circuits = connect(sorted_pairs, n)
    circuit_lengths = sorted([len(c) for c in circuits], reverse=True)
    return math.prod(circuit_lengths[:3])


def solve2(data):
    data_dict = parse_data(data)
    all_boxes_count = len(data_dict)
    distance_dict = calculate_distances(data_dict)
    sorted_pairs = sorted(distance_dict.items(), key=lambda item: item[1])
    return connect2(sorted_pairs, all_boxes_count)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, 1000)
    print(f'Example1: {result}')
    result = solve2(input_data)
    print(f'Example2: {result}')
