"""

https://adventofcode.com/2023/day/5

"""
import re
from dataclasses import dataclass


def convert_single_range(input_range, source_range, destination_range):
    # return input_ranges, output_ranges

    if input_range.start in source_range:
        if (input_range.stop - 1) in source_range:
            #  C  AB  D
            new_start = source_range.index(input_range.start)
            return (
                [],
                [destination_range[new_start: new_start + len(input_range)]]
            )
        else:
            #  C  A  D  B
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
    elif input_range.start not in source_range and input_range.stop not in source_range:
        # AB CD
        # CD AB
        return [input_range], []


@dataclass
class Map:
    id: str
    destinations: list[range]
    sources: list[range]
    lengths: list[int]

    def convert(self, source):
        for d, s, in zip(self.destinations, self.sources):
            if source in s:
                return d[s.index(source)]
        return source

    def __str__(self):
        return self.id

    def convert_ranges(self, input_range_list):
        input_ranges = input_range_list
        result_ranges = []

        for d, s, in zip(self.destinations, self.sources):
            new_input_ranges = []
            for in_range in input_ranges:
                a, b = convert_single_range(in_range, s, d)
                result_ranges += b
                new_input_ranges += a
            input_ranges = new_input_ranges

        print(self.id)
        print(result_ranges + input_ranges)

        return result_ranges + input_ranges

def get_seeds(data):
    seeds_line = data.split('\n\n')[0]
    seeds_list = [
        (int(i), int(j))
        for i, j in re.findall(r'(\d+) (\d+)', seeds_line)
    ]
    for i, j in seeds_list:
        seeds_range = range(i, i + j)
        for x in seeds_range:
            yield x


def parse_seeds(data):
    return [
        int(i)
        for i in re.findall(r'(\d+)', data.split('\n\n')[0])
    ]


def parse_maps(data):
    maps = {}
    for map_data in data.strip().split('\n\n')[1:]:
        print(map_data)
        map_lines = map_data.split('\n')
        id = map_lines[0].replace(' map:', '')
        destinations = []
        sources = []
        lengths = []
        for line in map_lines[1:]:
            nums = [int(i) for i in re.findall(r'(\d+)', line)]
            destinations.append(range(nums[0], nums[0] + nums[2]))
            sources.append(range(nums[1], nums[1] + nums[2]))
            lengths.append(nums[2])
        maps[id] = Map(id, destinations, sources, lengths)
    return maps


def convert_seed_to_location(seed, maps):
    result = maps['seed-to-soil'].convert(seed)

    result = maps['soil-to-fertilizer'].convert(result)
    result = maps['fertilizer-to-water'].convert(result)
    result = maps['water-to-light'].convert(result)
    result = maps['light-to-temperature'].convert(result)
    result = maps['temperature-to-humidity'].convert(result)
    result = maps['humidity-to-location'].convert(result)
    return result


def solve(data):
    seeds = parse_seeds(data)
    maps = parse_maps(data)
    return min([convert_seed_to_location(seed, maps) for seed in seeds])


#########################
### Part 2 ###########
from itertools import zip_longest

def get_seeds(data):
    # All numbers from the first line as integers
    data = map(int, re.findall(r'(\d+)', data.split('\n\n')[0]))
    return [
        range(start, start + length)
        for start, length in
        # in python 3.12 can be replaced with itertools.batched(iterable, n)
        zip_longest(*[iter(data)] * 2)
    ]


def convert_seed_to_location_2(seed_ranges, maps):

    #print('START', seed_ranges)
    result = maps['seed-to-soil'].convert_ranges(seed_ranges)
    #print(result)
    result = maps['soil-to-fertilizer'].convert_ranges(result)
    #print(result)
    result = maps['fertilizer-to-water'].convert_ranges(result)
    #print(result)
    result = maps['water-to-light'].convert_ranges(result)
    #print(result)
    result = maps['light-to-temperature'].convert_ranges(result)
    #print(result)
    result = maps['temperature-to-humidity'].convert_ranges(result)
    #print(result)
    result = maps['humidity-to-location'].convert_ranges(result)
    #print('END', result)
    return result


def solve_2(data):
    seeds = get_seeds(data)
    maps = parse_maps(data)
    result_ranges = convert_seed_to_location_2(seeds, maps)
    return min([i.start for i in result_ranges])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
