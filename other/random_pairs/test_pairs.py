from string import ascii_uppercase
import pytest

from .pairs import pull_pairs

TEAM_ODD = ['Jane', 'John', 'Jack']
TEAM_EVEN = ['Anne', 'Ben', 'Chuck', 'Dorothy']

TEAM_LONG = list(ascii_uppercase)
TEAM_SHORT = ['Jane', 'John']


@pytest.mark.parametrize('team', [TEAM_ODD, TEAM_EVEN, TEAM_LONG, TEAM_SHORT])
def test_right_number_of_pairs_is_pulled(team):
    pairs = pull_pairs(team)
    assert len(team) == len(pairs)


@pytest.mark.parametrize('team', [TEAM_ODD, TEAM_EVEN, TEAM_LONG, TEAM_SHORT])
def test_each_pair_contains_two_different_team_members(team):
    pairs = pull_pairs(team)
    assert all(len(set(pair)) == 2 for pair in pairs)


@pytest.mark.parametrize('team', [TEAM_ODD, TEAM_EVEN, TEAM_LONG, TEAM_SHORT])
def test_each_team_member_is_pulled_twice(team):
    pairs = pull_pairs(team)
    scrum_master = sorted([pair[0] for pair in pairs])
    backup_scrum_master = sorted([pair[1] for pair in pairs])
    assert sorted(team) == scrum_master == backup_scrum_master


def test_pairs_are_random():
    pairs1 = pull_pairs(TEAM_LONG)
    pairs2 = pull_pairs(TEAM_LONG)
    pairs3 = pull_pairs(TEAM_LONG)
    assert not (pairs1 == pairs2 == pairs3)


@pytest.mark.parametrize('team', [[], ['John'], ['John', 'John']])
def test_invalid_team_raises(team):
    with pytest.raises(ValueError):
        pull_pairs(team)
