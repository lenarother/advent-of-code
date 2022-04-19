"""Day 22: Wizard Simulator 20XX

https://adventofcode.com/2015/day/22

"""

import heapq
import re
from itertools import count

# hit points - always reduced at least 1
# damage = attacker's damage score - defender's armour score

BOSS = re.compile(r'Hit Points: (\d+)\nDamage: (\d+)\n')
SPELLS = ['missile', 'shield', 'poison', 'recharge', 'drain']


class Spell:

    def __init__(self):
        self.cost = None
        self.duration = 1

    def __repr__(self):
        return f'<{self.__class__.__name__}: {self.cost}, {self.duration}>'

    def __eq__(self, other):
        return self.__class__.__name__ == other.__class__.__name__

    @property
    def is_active(self):
        return self.duration > 0

    def effect(self, wizard, boss):
        pass

    def cast(self, wizard, boss):
        if self.is_active:
            self.effect(wizard=wizard, boss=boss)
            self.duration -= 1

    def copy(self):
        spell = self.__class__()
        spell.cost = self.cost
        spell.duration = self.duration
        return spell


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

        self.spells = []
        self.mana_used = 0

    def __repr__(self):
        return f'<Wizard: {self.hp}-{self.mana}-{self.armor}'

    @property
    def alive(self):
        return self.hp > 0 and self.mana >= 0

    @property
    def active_spells(self):
        return (s for s in self.spells if s.is_active)

    def die(self):
        self.hp = -1000

    def pay(self, cost):
        if cost > self.mana:
            self.die()
        self.mana -= cost
        self.mana_used += cost

    def buy(self, spell):
        if spell in self.active_spells:
            self.die()
        self.pay(spell.cost)
        self.spells.append(spell)

    def cast(self, boss):
        for s in self.spells:
            s.cast(self, boss)

    def fight_round(self, boss, spell_name, hard=False):
        if hard:
            self.hp -= 1
            if self.hp <= 0:
                self.die()
        spell = spell_factory(spell_name)
        self.buy(spell)
        self.cast(boss)
        boss.hit(self)
        self.cast(boss)

    def copy(self):
        wizard = Wizard(hp=self.hp, mana=self.mana, armor=self.armor)
        wizard.spells = [s.copy() for s in self.spells]
        wizard.mana_used = self.mana_used
        return wizard


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

    def copy(self):
        return Boss(self.hp, self.damage)


def parse_boss(input_str):
    hp, damage = map(int, list(BOSS.findall(input_str)[0]))
    return Boss(hp, damage)


def find_best_spells(wizard, boss, hard=False):
    # Dijkstra algorithm
    counter = count()  # use to avoid equal cost and wizard compering
    fights = []
    heapq.heappush(fights, (wizard.mana_used, next(counter), (wizard, boss)))

    while fights:
        mana_used, _, (wizard, boss) = heapq.heappop(fights)
        if not boss.alive:
            return mana_used
        for s in SPELLS:
            wizard_copy = wizard.copy()
            boss_copy = boss.copy()
            wizard_copy.fight_round(boss_copy, s, hard)
            if wizard_copy.alive:
                heapq.heappush(
                    fights,
                    (
                        wizard_copy.mana_used,
                        next(counter),
                        (wizard_copy, boss_copy)
                    )
                )

    return -1


def solve(input_data, hard=False):
    boss = parse_boss(input_data)
    wizard = Wizard(hp=50, mana=500)
    return find_best_spells(wizard, boss, hard)


if __name__ == '__main__':
    data = open('input_data.txt').read()
    result = solve(data)
    print(f'Example1: {result}')

    result = solve(data, hard=True)
    print(f'Example2: {result}')
