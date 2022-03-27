"""Day 21: RPG Simulator 20XX

https://adventofcode.com/2015/day/21

"""
import re
from dataclasses import dataclass
from itertools import combinations, product

# hit points - always reduced at least 1
# damage = attacker's damage score - defender's armour score
# user 0 damage , 0 armour, 100 hit points

SHOP = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0
Shortsword   10     5       0
Warhammer    25     6       0
Longsword    40     7       0
Greataxe     74     8       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2
Splintmail   53     0       3
Bandedmail   75     0       4
Platemail   102     0       5

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
Defense +1   20     0       1
Defense +2   40     0       2
Defense +3   80     0       3
"""


BOSS = re.compile(r'Hit Points: (\d+)\nDamage: (\d+)\nArmor: (\d+)')
ITEM = re.compile(r'\w+\s?\+?\d?\s+(\d+)\s+(\d+)\s+(\d+)')


class Character:

    def __init__(self, hp, damage, armor):
        self.hp = hp
        self.damage = damage
        self.armor = armor

    def __repr__(self):
        return f'<Character: {self.hp}-{self.damage}-{self.armor}'

    def fight(self, opponent):
        """Return True in case of win"""
        while self.hp > 0 and opponent.hp > 0:
            opponent.hp -= max(self.damage - opponent.armor, 1)
            self.hp -= max(opponent.damage - self.armor, 1)
        return opponent.hp <= 0


@dataclass
class Item:
    cost: int
    damage: int = 0
    armor: int = 0

    def __add__(self, other):
        return Item(
            self.cost + other.cost,
            self.damage + other.damage,
            self.armor + other.armor,
        )


def parse_character(input_str):
    hp, damage, armor = map(int, list(BOSS.findall(input_str)[0]))
    return Character(hp, damage, armor)


def _parse_item_list_from_string(item_list_str):
    return [
        Item(int(cost), int(damage), int(armor))
        for cost, damage, armor in ITEM.findall(item_list_str)
    ]


def parse_shop(input_str):
    for items_str in input_str.strip().split('\n\n'):
        yield _parse_item_list_from_string(items_str)


def item_combinations(weapons, armors, rings):
    ring_pairs = combinations(rings, 2)
    for w, a, rp in product(weapons, armors, ring_pairs):
        yield w + a + rp[0] + rp[1]


def go_shopping(weapons, armors, rings):
    empty_item = Item(0, 0, 0)
    armors.append(empty_item)
    rings.extend([empty_item, empty_item])
    return item_combinations(weapons, armors, rings)


def solve(data, shop, price_function=min):
    return price_function([
        item.cost
        for item in go_shopping(*parse_shop(shop))
        if Character(
            100, item.damage, item.armor
        ).fight(parse_character(data)) is (price_function == min)
    ])


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data, SHOP, min)
    print(f'Example1: {result}')

    result = solve(input_data, SHOP, max)
    print(f'Example2: {result}')
