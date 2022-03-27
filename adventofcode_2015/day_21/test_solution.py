import pytest

from .solution import (
    Character,
    Item,
    go_shopping,
    item_combinations,
    parse_character,
    parse_shop,
    solve,
)

INPUT_DATA = """
Hit Points: 100
Damage: 8
Armor: 2
"""

SHOP_1 = """
Weapons:    Cost  Damage  Armor
Dagger        8     4       0

Armor:      Cost  Damage  Armor
Leather      13     0       1
Chainmail    31     0       2

Rings:      Cost  Damage  Armor
Damage +1    25     1       0
Damage +2    50     2       0
Damage +3   100     3       0
"""

SHOP_2 = """
Weapons:    Cost  Damage  Armor
Dagger       10     999       0
Sword        11     999       0
RubberDuck  999       1       0

Armor:      Cost  Damage  Armor
dummy1       999      0       0

Rings:      Cost  Damage  Armor
dummy2       999      0       0
"""


def test_parse_character():
    boss = parse_character(INPUT_DATA)
    assert boss.hp == 100
    assert boss.damage == 8
    assert boss.armor == 2


def test_parse_shop():
    weapons, armors, rings = parse_shop(SHOP_1)
    assert len(weapons) == 1
    assert len(armors) == 2
    assert len(rings) == 3


def test_add_items():
    item_1 = Item(1, 2, 3)
    item_2 = Item(4, 5, 6)
    assert item_1 + item_2 == Item(5, 7, 9)


def test_get_item_combinations():
    weapon = Item(1, 2, 3)
    armor = Item(4, 5, 6)
    ring1 = Item(0, 0, 0)
    ring2 = Item(8, 9, 10)

    items = list(item_combinations([weapon], [armor], [ring2, ring1]))
    item = items[0]

    assert len(items) == 1
    assert item == Item(13, 16, 19)


def test_get_item_combinations_items_empty():
    weapon = Item(1, 2, 3)
    items = list(item_combinations([weapon], [], []))
    assert items == []


def test_items_equal():
    weapon = Item(1, 2, 3)
    armor = Item(4, 5, 6)
    ring = Item(1, 2, 3)

    assert weapon == weapon
    assert weapon == ring
    assert weapon != armor


def test_go_shopping_empty():
    weapon = Item(1, 2, 3)
    items = list(go_shopping([weapon], [], []))
    item = items[0]

    assert len(items) == 1
    assert item == weapon


def test_go_shopping():
    weapon = Item(1, 2, 3)
    armor = Item(4, 5, 6)
    ring = Item(8, 9, 10)
    items = list(go_shopping([weapon], [armor], [ring]))

    assert len(items) == 6


@pytest.mark.parametrize(
    'ch1,ch2,expected',
    (
        (Character(hp=1, damage=1, armor=0), Character(hp=10, damage=10, armor=0), False),  # noqa
        (Character(hp=10, damage=10, armor=0), Character(hp=1, damage=1, armor=0), True),  # noqa
        (Character(hp=10, damage=1, armor=0), Character(hp=5, damage=100, armor=0), False),  # noqa
        (Character(hp=10, damage=1, armor=0), Character(hp=1, damage=100, armor=0), True),  # noqa
        (Character(hp=2, damage=1, armor=0), Character(hp=2, damage=1, armor=0), True),  # noqa
        (Character(hp=2, damage=1, armor=0), Character(hp=3, damage=1, armor=0), False),  # noqa
        (Character(hp=2, damage=2, armor=0), Character(hp=3, damage=1, armor=0), True),  # noqa
        (Character(hp=1, damage=0, armor=0), Character(hp=1, damage=1, armor=0), True),  # noqa

        # With armor
        (Character(hp=1, damage=0, armor=0), Character(hp=1, damage=1, armor=1), True),  # noqa
        (Character(hp=1, damage=5, armor=0), Character(hp=5, damage=1, armor=5), False),  # noqa
    )
)
def test_find_winner(ch1, ch2, expected):
    assert ch1.fight(ch2) is expected


@pytest.mark.parametrize(
    'price_function,expected',
    (
        (min, 10),
        (max, 2997),
    )
)
def test_solve(price_function, expected):
    assert solve(INPUT_DATA, SHOP_2, price_function) == expected
