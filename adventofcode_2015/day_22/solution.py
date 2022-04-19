"""Day 22: Wizard Simulator 20XX

https://adventofcode.com/2015/day/22

"""

import re
import heapq
from copy import deepcopy

from itertools import count

# hit points - always reduced at least 1
# damage = attacker's damage score - defender's armour score
# user 0 damage , 0 armour, 100 hit points

BOSS = re.compile(r'Hit Points: (\d+)\nDamage: (\d+)\n')
SPELLS = ['missile', 'shield', 'poison', 'recharge', 'drain']


class Spell:

    def __init__(self):
        self.cost = None
        self.duration = 1

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.cost}, {self.duration}>'

    @property
    def is_active(self):
        return self.duration > 0

    def effect(self, wizard, boss):
        pass

    def cast(self, wizard, boss):
        if self.is_active:
            self.effect(wizard=wizard, boss=boss)
            self.duration -= 1


class SpellShield(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 113
        self.duration = 6

    def effect(self, wizard, boss):
        wizard.armor = 7

    def cast(self, wizard, boss):
        super().cast(wizard, boss)
        if not self.is_active:
            wizard.armor = 0


class SpellMissile(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 53

    def effect(self, wizard, boss):
        boss.hp -= 4


class SpellPoison(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 173
        self.duration = 6

    def effect(self, wizard, boss=None):
        boss.hp -= 3


class SpellRecharge(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 229
        self.duration = 5

    def effect(self, wizard, boss=None):
        wizard.mana += 101


class SpellDrain(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 73

    def effect(self, wizard, boss=None):
        wizard.hp += 2
        boss.hp += -2


def spell_factory(name):
    return {
        'missile': SpellMissile,
        'shield': SpellShield,
        'poison': SpellPoison,
        'recharge': SpellRecharge,
        'drain': SpellDrain,
    }[name]()


class Wizard:

    def __init__(self, hp, mana, armor=0):
        self.hp = hp
        self.mana = mana
        self.armor = armor

        self.mana_used = 0
        self.spells = []

    def __repr__(self):
        return f'<Wizard: {self.hp}-{self.mana}-{self.armor}'

    @property
    def alive(self):
        return self.hp > 0 and self.mana >= 0

    def die(self):
        self.hp = -1000

    def pay(self, cost):
        if cost > self.mana:
            self.die()
        self.mana -= cost
        self.mana_used += cost

    def buy(self, spell):
        self.pay(spell.cost)
        self.spells.append(spell)

    def cast(self, boss):
        for s in self.spells:
            s.cast(self, boss)

    def fight_round(self, boss, spell_name):
        spell = spell_factory(spell_name)
        self.buy(spell)
        self.cast(boss)
        self.cast(boss)
        boss.hit(self)


class Boss:

    def __init__(self, hp, damage):
        self.hp = hp
        self.damage = damage

    def __repr__(self):
        return f'<Boss: {self.hp}-{self.damage}'

    @property
    def alive(self):
        return self.hp > 0

    def hit(self, wizard):
        if self.alive:
            wizard.hp -= max(self.damage - wizard.armor, 1)


def parse_boss(input_str):
    hp, damage = map(int, list(BOSS.findall(input_str)[0]))
    return Boss(hp, damage)


def find_best_spells(wizard, boss):
    # Dijkstra algorithm
    counter = count()

    fights = []
    heapq.heappush(fights, (wizard.mana_used, next(counter), (wizard, boss)))

    while fights:
        mana_used, _, (wizard, boss) = heapq.heappop(fights)
        if not boss.alive:
            # print(wizard.spells)
            return mana_used
        for s in SPELLS:
            # print(s)
            wizard_copy = deepcopy(wizard)
            boss_copy = deepcopy(boss)
            # print(wizard_copy)
            # print(boss_copy)
            wizard_copy.fight_round(boss_copy, s)
            # print(wizard_copy)
            # print(boss_copy)
            if wizard_copy.alive:
                heapq.heappush(fights, (wizard_copy.mana_used, next(counter), (wizard_copy, boss_copy)))

    return -1


def solve(input_data):
    boss = parse_boss(input_data)
    wizard = Wizard(hp=50, mana=500)
    return find_best_spells(wizard, boss)


if __name__ == '__main__':
    data = open('input_data.txt').read()
    result = solve(data)
    print(f'Example1: {result}')
