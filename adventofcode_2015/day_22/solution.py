"""Day 22: Wizard Simulator 20XX

https://adventofcode.com/2015/day/22

"""

import re
import heapq
from copy import copy, deepcopy

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

    def cast(self, wizard=None, boss=None):
        if self.is_active:
            self.effect(wizard=wizard, boss=boss)
            self.duration -= 1


class SpellShield(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 113
        self.duration = 6

    def effect(self, wizard, boss=None):
        wizard.armor = 7

    def cast(self, wizard, boss=None):
        super().cast(wizard, boss)
        if not self.is_active:
            wizard.armor = 0


class SpellMissile(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 53

    def effect(self, wizard, boss):
        print('HIE')
        boss.hp -= 4


class SpellPoison(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 173
        self.duration = 6

    def effect(self, wizard, boss=None):
        boss.hp = 3


class SpellRecharge(Spell):

    def __init__(self):
        super().__init__()
        self.cost = 229
        self.duration = 5

    def effect(self, wizard, boss=None):
        wizard.mana = 101


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

        # self.ongoing_spells = []
        # self.history = []

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

    # def shield(self, boss=None, initial_call=True):
    #     if initial_call:
    #         self.pay(113)
    #         self.ongoing_spells.append(('shield', 6))
    #     self.armor = 7
    #
    # def missile(self, boss):
    #     self.pay(53)
    #     boss.hp -= 4
    #
    # def poison(self, boss, initial_call=True):
    #     if initial_call:
    #         self.pay(173)
    #         self.ongoing_spells.append(('poison', 6))
    #     else:
    #         boss.hp -= 3
    #
    # def recharge(self, boss=None, initial_call=True):
    #     if initial_call:
    #         # if self.mana > 300:
    #         #     self.die()
    #         self.pay(229)
    #         self.ongoing_spells.append(('recharge', 5))
    #     else:
    #         self.mana += 101
    #
    # def drain(self, boss):
    #     self.pay(73)
    #     self.hp += 2
    #     boss.hp -= 2

    # def apply_ongoing_spells(self, boss):
    #     new_ongoing_spells = []
    #     for spell in self.ongoing_spells:
    #         s, counter = spell
    #         f = getattr(self, s)
    #         f(boss, initial_call=False)
    #         if counter >= 1:
    #             new_ongoing_spells.append((s, counter - 1))
    #         elif s == 'shield':
    #             self.armor = 0
    #     self.ongoing_spells = new_ongoing_spells
    #
    # def cast_spell(self, boss, spell):
    #     self.apply_ongoing_spells(boss)
    #     if boss.alive:
    #         if spell in [s[0] for s in self.ongoing_spells]:
    #             self.die()
    #         f = getattr(self, spell)
    #         f(boss)
    #         self.history.append(spell)
    #         self.apply_ongoing_spells(boss)

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

    def __init__(self, hp, damage, armor=0):
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
            # spell = spell_factory(s)
            # wizard_copy.buy(spell)
            # wizard_copy.cast(boss_copy)
            # wizard_copy.cast(boss_copy)
            # boss_copy.hit(wizard_copy)

            # print(wizard_copy)
            # print(boss_copy)

            if wizard_copy.alive:
                heapq.heappush(fights, (wizard_copy.mana_used, next(counter), (wizard_copy, boss_copy)))

            # wizard_copy = deepcopy(wizard)
            # boss_copy = deepcopy(boss)
            # wizard_copy.cast_spell(boss_copy, s)
            # boss_copy.hit(wizard_copy)
            # if wizard_copy.alive:
            #     heapq.heappush(fights, (wizard_copy.mana_used, next(counter), (wizard_copy, boss_copy)))

    return -1


def solve(input_data):
    boss = parse_boss(input_data)
    wizard = Wizard(hp=50, mana=500)
    return find_best_spells(wizard, boss)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

