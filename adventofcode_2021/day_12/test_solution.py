import pytest

from .solution import Cave, solve

DATA_SMALL = """
start-A
start-b
A-c
A-b
b-d
A-end
b-end"""

DATA_MEDIUM = """
dc-end
HN-start
start-kj
dc-start
dc-HN
LN-dc
HN-end
kj-sa
kj-HN
kj-dc"""

DATA_LARGE = """
fs-end
he-DX
fs-he
start-DX
pj-DX
end-zg
zg-sl
zg-pj
pj-he
RW-he
fs-DX
pj-RW
zg-RW
start-pj
he-WI
zg-he
pj-fs
start-RW"""

EXAMPLES = (
    (DATA_SMALL, 10),
    (DATA_MEDIUM, 19),
    (DATA_LARGE, 226),
)

EXAMPLES_VISIT_TWICE = (
    (DATA_SMALL, 36),
    (DATA_MEDIUM, 103),
    (DATA_LARGE, 3509),
)

EXAMPLE_PARSE = (
    (DATA_SMALL, {
        'start': {'A', 'b'},
        'A': {'c', 'b', 'end'},
        'b': {'d', 'A', 'end'},
        'c': {'A'},
        'd': {'b'},
    }),
)

EXAMPLES_CAN_ADD = (
    ('A', [], True),
    ('a', [], True),
    ('A', ['A', 'A', 'A'], True),
    ('a', ['A', 'A', 'A'], True),
    ('a', ['a', 'A', 'A'], True),
    ('a', ['a', 'a', 'A'], False),
    ('a', ['c', 'c', 'A'], True),
    ('a', ['c', 'd', 'A'], True),

)


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve_no_lowercase_duplicates(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_VISIT_TWICE)
def test_solve_at_most_single_duplicate(data, expected):
    assert solve(data, mode='single_duplicate') == expected


@pytest.mark.parametrize('data,expected', EXAMPLE_PARSE)
def test_parse(data, expected):
    assert Cave.parse(data) == expected


@pytest.mark.parametrize('node,path,expected', EXAMPLES_CAN_ADD)
def test_can_add(node, path, expected):
    assert Cave().has_at_most_one_lowercase_duplicate(node, path) == expected
