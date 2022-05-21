from .solution import solve, solve2

DATA = """
aa bb cc dd ee
aa bb cc dd aa
aa bb cc dd aaa
"""

DATA_ANAGRAMS = """
abcde fghij.
abcde xyz ecdab
a ab abc abd abf abj
iiii oiii ooii oooi oooo
oiii ioii iioi iiio
"""


def test_solve():
    assert solve(DATA) == 2


def test_solve2():
    assert solve2(DATA_ANAGRAMS) == 3
