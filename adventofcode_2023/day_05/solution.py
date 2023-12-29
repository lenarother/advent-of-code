"""

https://adventofcode.com/2023/day/5

"""
import re
from dataclasses import dataclass
from itertools import zip_longest


def convert_single_range(
        input_range: range,
        source_range: range,
        destination_range: range
) -> tuple[list[range], list[range]]:
    """Map single range.

    For Part 2.
    Convert input range to
    remaining input range(s) and destination range(s).
    If input range is disconnected with source range,
    output will contain original input range and no destination ranges.

    Possible situations:
    C  AB  D -> input range inside source
    C  A  D  B / A  C  B  D -> overlap
    A  CD  B -> source inside input range
    AB CD / CD AB -> disconnected

    Args:
        input_range: range to convert (AB)
        source_range: range that may contain input range (CD)
        destination_range: range corresponding to source

    Returns:
        list of remaining input ranges (0, 1 or 2)
        list of destination ranges (0, 1 or 2)
    """
    if input_range.start in source_range:
        if (input_range.stop - 1) in source_range:
            # C  AB  D
            new_start = source_range.index(input_range.start)
            return (
                [],
                [destination_range[new_start: new_start + len(input_range)]]
            )
        else:
            # C  A  D  B
            new_start = source_range.index(input_range.start)
            new_range = destination_range[new_start:]
            return (
                [input_range[len(new_range):]],
                [new_range]
            )
    elif source_range.start in input_range:
        if (source_range.stop - 1) in input_range:
            # A  CD  B
            return (
                [
                    range(input_range.start, source_range.start),
                    range(source_range.stop, input_range.stop)
                ],
                [destination_range]
            )
        else:
            # A  C  B  D
            new_stop = source_range.index(input_range.stop)
            return (
                [range(input_range.start, source_range.start)],
                [destination_range[:new_stop]]
            )
    else:
        # disconnected
        # AB CD
        # CD AB
        return [input_range], []


@dataclass
class Map:
    """Conversion map"""
    id: str
    destinations: list[range]
    sources: list[range]

    def __str__(self):
        return self.id

    def convert(self, source: int) -> int:
        """Part 1: Convert single number into destination number."""
        for d, s, in zip(self.destinations, self.sources):
            if source in s:
                return d[s.index(source)]
        return source

    def convert_ranges(self, input_ranges: list[range]) -> list[range]:
        """Part 2: Convert input range into destination ranges."""
        result_ranges = []

        for d, s, in zip(self.destinations, self.sources):
            new_input_ranges = []
            for in_range in input_ranges:
                a, b = convert_single_range(in_range, s, d)
                result_ranges += b
                new_input_ranges += a
            input_ranges = new_input_ranges

        return result_ranges + input_ranges


def parse_seeds(data: str) -> list[int]:
    """Part 1: Return list of seeds."""
    return [
        int(i)
        for i in re.findall(r'(\d+)', data.split('\n\n')[0])
    ]


def get_seed_ranges(data: str) -> list[range]:
    """Part 2: Return list of seed ranges."""
    # All numbers from the first line as integers
    data_nums = map(int, re.findall(r'(\d+)', data.split('\n\n')[0]))
    return [
        range(start, start + length)
        for start, length in
        # in python 3.12 can be replaced with itertools.batched(iterable, n)
        zip_longest(*[iter(data_nums)] * 2)
    ]


def parse_maps(data: str) -> dict[str, Map]:
    """Parse input string into Map objects.

    Return dictionary of maps with their ids as keys.
    """
    maps = {}
    for map_data in data.strip().split('\n\n')[1:]:
        map_lines = map_data.split('\n')
        id = map_lines[0].replace(' map:', '')
        destinations = []
        sources = []
        for line in map_lines[1:]:
            nums = [int(i) for i in re.findall(r'(\d+)', line)]
            destinations.append(range(nums[0], nums[0] + nums[2]))
            sources.append(range(nums[1], nums[1] + nums[2]))
        maps[id] = Map(id, destinations, sources)
    return maps


def convert_seed_to_location(seed: int, maps: dict) -> int:
    result = maps['seed-to-soil'].convert(seed)
    result = maps['soil-to-fertilizer'].convert(result)
    result = maps['fertilizer-to-water'].convert(result)
    result = maps['water-to-light'].convert(result)
    result = maps['light-to-temperature'].convert(result)
    result = maps['temperature-to-humidity'].convert(result)
    result = maps['humidity-to-location'].convert(result)
    return result


def convert_seed_range_to_location_range(
        seed_ranges: list[range],
        maps: dict
) -> list[range]:
    result = maps['seed-to-soil'].convert_ranges(seed_ranges)
    result = maps['soil-to-fertilizer'].convert_ranges(result)
    result = maps['fertilizer-to-water'].convert_ranges(result)
    result = maps['water-to-light'].convert_ranges(result)
    result = maps['light-to-temperature'].convert_ranges(result)
    result = maps['temperature-to-humidity'].convert_ranges(result)
    result = maps['humidity-to-location'].convert_ranges(result)
    return result


def solve(data: str) -> int:
    seeds = parse_seeds(data)
    maps = parse_maps(data)
    return min([convert_seed_to_location(seed, maps) for seed in seeds])


def solve_2(data: str) -> int:
    seeds = get_seed_ranges(data)
    maps = parse_maps(data)
    result_ranges = convert_seed_range_to_location_range(seeds, maps)
    return min([i.start for i in result_ranges])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
