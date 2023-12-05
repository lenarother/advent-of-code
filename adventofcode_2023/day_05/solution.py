"""

https://adventofcode.com/2023/day/5

"""
import re
from dataclasses import dataclass


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


def solve_2(data):
    seeds = get_seeds(data)
    maps = parse_maps(data)
    return min([convert_seed_to_location(seed, maps) for seed in seeds])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example2: {result}')
