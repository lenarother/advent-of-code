"""Day 19: Not Enough Minerals

https://adventofcode.com/2022/day/19

"""
import re

ORE = 'ore'
CLAY = 'clay'
OBSIDIAN = 'obsidian'
GEODE = 'geode'

BLUEPRINT_RE = re.compile(
    r'Blueprint (\d+): '
    r'Each ore robot costs (\d+) ore. '
    r'Each clay robot costs (\d+) ore. '
    r'Each obsidian robot costs (\d+) ore and (\d+) clay. '
    r'Each geode robot costs (\d+) ore and (\d+) obsidian.'
)


class Blueprint:
    def __init__(self, id):
        self.id = id
        ore = None
        clay = None
        obsidian = None
        geode = None



def parse(data):
    for x in BLUEPRINT_RE.findall(data):
        b = Blueprint(x[0])
        # robot = (cost_dict, produced_resource)
        b.ore = ({ORE: x[1]}, ORE)
        b.clay = ({ORE: x[2]}, CLAY)
        b.obsidian = ({ORE: x[3], CLAY: x[4]}, OBSIDIAN)
        b.geode = ({ORE: x[5], OBSIDIAN: x[6]}, GEODE)
        yield b


def get_max_geodes(blueprint):
    robots = [blueprint.ore]
    resources = {
        ORE: 0,
        CLAY: 0,
        OBSIDIAN: 0,
        GEODE: 0,
    }


def collect(robots, resources):
    for r in robots:
        resources[r[1]] += 1


def buy(robots, resources):
    pass



def solve(data):
    return sum([b.id * get_max_geodes(b) for b in parse(data)])



if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
