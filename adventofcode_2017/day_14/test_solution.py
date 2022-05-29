from .solution import get_occupied_addresses, solve, solve2


def test_solve():
    assert solve('amgozmfv') == 8222


def test_hashes_to_dict():
    assert len(get_occupied_addresses('amgozmfv')) == 8222


def test_solve2():
    assert solve2('flqrgnkx') == 1242
