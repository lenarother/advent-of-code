"""Day 19: Medicine for Rudolph

https://adventofcode.com/2015/day/19

"""
import heapq
import re
from collections import defaultdict

REPLACEMENT = re.compile(r'(\w+) => (\w+)')


def parse_instructions(data):
    replacements = defaultdict(set)
    for orig, replacement in REPLACEMENT.findall(data):
        replacements[orig].add(replacement)
    return replacements


def parse_instructions_reverse(data):
    return {
        replacement: orig
        for orig, replacement in REPLACEMENT.findall(data)
    }


def parse(data, instruction_parse_function):
    instructions, molecule = data.strip().split('\n\n')
    return molecule, instruction_parse_function(instructions)


def molecule_fragments():
    """Manually splited molecule for part 2."""
    return [
        'ORnPBPMgArCaCaCaSiThCaCaSiThCaCaPB',
        'SiRnFArRnFArCaCaSiThCaCaSiThCaCaCaCaCaCa',
        'SiRnFYFAr',
        'SiRnMgArCa',
        'SiRnPTiTiBFYPBFAr',
        'SiRnCa',
        'SiRnTiRnFArSiAlArPTiBPTiRnCaSiAlArCaPTiTiBPMgYFArPTiRnFAr',
        'SiRnCaCaFArRnCaFArCa',
        'SiRn',
        'SiRnMgArFYCa',
        'SiRnMgArCaCaSiThPRnFArPBCa',
        'SiRnMgArCaCaSiThCa',
        'SiRnTiMgArFArSiThSiThCaCa',
        'SiRnMgArCaCa',
        'SiRnFArTiBPTiRnCaSiAlArCaPTiRnFArPBPB',
        'CaCaSiThCaPBSiThPRnFArSiThCaSiThCaSiThCaPTiB',
        'SiRnFYFArCaCaPRnFArPBCaCaPB',
        'SiRnTiRnFArCaPRnFAr',
        'SiRnCaCaCaSiThCaRnCaFArYCa',
        'SiRnFArBCaCaCaSiThFArPBFArCa',
        'SiRnFArRnCaCaCaFAr',
        'SiRnFArTiRnPMgArF',
    ]


def molecule_generator(m, replacements):
    for r in replacements:
        pattern = re.compile(r)
        for occurrence in pattern.finditer(m):
            for option in replacements[r]:
                yield (
                    f'{m[:occurrence.start()]}'
                    f'{option}'
                    f'{m[occurrence.end():]}'
                )


def molecule_reverse_generator(m, inverted_replacements):
    instructions = list(inverted_replacements.items())
    instructions.sort(key=lambda x: len(x[0]), reverse=True)
    for k, v in instructions:
        pattern = re.compile(k)
        for occurrence in pattern.finditer(m):
            yield (
                f'{m[:occurrence.start()]}'
                f'{v}'
                f'{m[occurrence.end():]}'
            )


def solve_fragment(target='e', replacements=None, molecule=''):
    i = 0
    m = molecule
    visited = {m}
    molecules_queue = []
    heapq.heappush(molecules_queue, (i, len(m), m))

    while 1:
        if len(molecules_queue) == 0:
            return i, m

        i, n, m = heapq.heappop(molecules_queue)
        if m == target:
            return i

        for x in molecule_reverse_generator(m, replacements):
            if x not in visited:
                heapq.heappush(molecules_queue, (i + 1, len(x), x))
                visited.add(x)


def solve(data):
    molecule, replacements = parse(data, parse_instructions)
    return len(set(molecule_generator(molecule, replacements)))


def solve2(data):
    _, replacements = parse(data, parse_instructions_reverse)
    molecule = molecule_fragments()
    last_fragment = ''
    count = 0

    for fragment in molecule:
        c, m = solve_fragment(molecule=fragment, replacements=replacements)
        count += c
        last_fragment += m

    count += solve_fragment(molecule=last_fragment, replacements=replacements)
    return count


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
