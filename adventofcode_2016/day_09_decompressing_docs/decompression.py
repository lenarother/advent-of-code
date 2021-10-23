"""Day 9: Explosives in Cyberspace

https://adventofcode.com/2016/day/9
"""
import re
from functools import reduce

PATTERN_SPLIT = r'\((\d+x\d+)\)'


def clean_text(text):
    return text.strip().replace(' ', '')


def get_marker(marker):
    return list(map(int, re.findall(r'(\d+)x(\d+)', marker)[0]))


def find_text_length(text, result=0):
    # PART 1
    parts = re.split(PATTERN_SPLIT, text, 1)
    if len(parts) == 1:
        result += len(parts[0])
        return result
    seq, marker, rest = parts
    i, repetitions = get_marker(marker)
    result += len(seq)
    result += len((rest[:i])) * repetitions
    new_text = rest[i:]
    return find_text_length(new_text, result)


def step(todo, done):
    # PART 2 UGLY
    parts = re.split(PATTERN_SPLIT, todo, 1)
    if len(parts) == 1:
        done += parts[0]
        todo = ''
    else:
        ready, marker, rest = parts
        i, repetitions = get_marker(marker)
        done += ready
        todo = ((rest[:i]) * repetitions) + rest[i:]
    return todo, done


def decompress(text):
    # PART 2 UGLY
    todo = clean_text(text)
    done = ''
    while todo:
        todo, done = step(todo, done)
    return len(done)


def product(markers):
    return reduce(lambda a, b: a * b[1], markers, 1)


def update_markers(markers):
    return [(a - 1, b) for a, b in markers if a > 1]


def add_marker(markers, m, len_m):
    markers = [(a - len_m, b) for a, b in markers if a > len_m]
    markers.append(m)
    return markers


def decompress_v2(text):
    # PART 2
    text = clean_text(text)
    i = 0
    total = 0
    markers = []

    while i < len(text):
        ch = text[i]
        if ch == '(':
            _, marker, _ = re.split(PATTERN_SPLIT, text[i:], 1)
            marker_length = len(marker) + 2
            new_marker = get_marker(marker)
            markers = add_marker(markers, new_marker, marker_length)
            i += marker_length
        else:
            total += product(markers)
            markers = update_markers(markers)
            i += 1

    return total


if __name__ == '__main__':
    text = clean_text(open('input_data.txt').read())
    print(f'Example1: {find_text_length(text)}')
    result = decompress_v2(open('input_data.txt').read())
    print(f'Example2: {result}')
