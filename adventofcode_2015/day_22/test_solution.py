import pytest

from .solution import (
    Boss,
    Wizard,
    find_best_spells,
    parse_boss,
)

INPUT_DATA = """
Hit Points: 71
Damage: 18
"""


# def test_parse_character():
#     boss = parse_boss(INPUT_DATA)
#     assert boss.hp == 71
#     assert boss.damage == 18


@pytest.mark.parametrize(
    'ch1,ch2,expected',
    (
        # 53 -> missile
        # 113 -> shield
        # 173 -> poison
        # 229 -> recharge
        # 73 -> drain
        (Wizard(hp=100, mana=500), Boss(hp=4, damage=1), 53),
        (Wizard(hp=100, mana=500), Boss(hp=5, damage=1), 2 * 53),
        (Wizard(hp=100, mana=500), Boss(hp=9, damage=1), 3 * 53),
        (Wizard(hp=5, mana=500), Boss(hp=5, damage=5), 73 + 53),
        (Wizard(hp=5, mana=500), Boss(hp=7, damage=5), 113 + 2 * 53),
        (Wizard(hp=100, mana=500), Boss(hp=30, damage=1), 173 + 3 * 53),
        (Wizard(hp=100, mana=229), Boss(hp=20, damage=1), 229 + 5 * 53),
        (Wizard(hp=1, mana=500), Boss(hp=5, damage=1), 73 + 53),
        (Wizard(hp=100, mana=20), Boss(hp=1, damage=1), -1),
        (Wizard(hp=100, mana=173), Boss(hp=18, damage=1), -1),
        (Wizard(hp=10, mana=250), Boss(hp=14, damage=8), 229 + 113 + 73 + 173 + 53),
        (Wizard(hp=1000, mana=1000), Boss(hp=60, damage=1), 173 + 3 * 53 + 173 + 3 * 53),
    ),
)
def test_find_best_spells(ch1, ch2, expected):
    assert find_best_spells(ch1, ch2) == expected


# def test_shield():
#     w = Wizard(hp=1000, mana=5000)
#     b = Boss(hp=1000, damage=1)
#     w.cast_spell(b, 'shield')
#     assert w.armor == 7
#     n = 5
#     while n:
#         w.apply_ongoing_spells(b)
#         assert w.armor == 7
#         n -= 1
#     w.apply_ongoing_spells(b)
#     assert w.armor == 0

# @pytest.mark.parametrize(
#     'wizard,boss,wizard_hp',
#     (
#         (Wizard(hp=100, mana=500), Boss(hp=5, damage=1), 99),
#         (Wizard(hp=100, mana=500, armor=5), Boss(hp=5, damage=5), 99),
#     ),
# )
# def test_boss_hits(wizard, boss, wizard_hp):
#     boss.hit(wizard)
#     assert wizard.hp == wizard_hp
