import pytest

from .solution import (
    add_expr,
    calc_magnitude,
    explode_expr,
    find_sum,
    solve,
    solve2,
    split_expr,
)

HOMEWORK_1 = """
[1,1]
[2,2]
[3,3]
[4,4]"""

HOMEWORK_2 = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]"""

HOMEWORK_3 = """
[1,1]
[2,2]
[3,3]
[4,4]
[5,5]
[6,6]
"""

HOMEWORK_4 = """
[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]
[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]
[[2,[[0,8],[3,4]]],[[[6,7],1],[7,[1,6]]]]
[[[[2,4],7],[6,[0,5]]],[[[6,8],[2,8]],[[2,1],[4,5]]]]
[7,[5,[[3,8],[1,4]]]]
[[2,[2,2]],[8,[8,1]]]
[2,9]
[1,[[[9,3],9],[[9,0],[0,7]]]]
[[[5,[7,4]],7],1]
[[[[4,2],2],6],[8,7]]"""

HOMEWORK_5 = """
[[[0,[5,8]],[[1,7],[9,6]]],[[4,[1,2]],[[1,4],2]]]
[[[5,[2,8]],4],[5,[[9,9],0]]]
[6,[[[6,2],[5,6]],[[7,6],[4,7]]]]
[[[6,[0,7]],[0,9]],[4,[9,[9,0]]]]
[[[7,[6,4]],[3,[1,3]]],[[[5,5],1],9]]
[[6,[[7,3],[3,2]]],[[[3,8],[5,7]],4]]
[[[[5,4],[7,7]],8],[[8,3],8]]
[[9,3],[[9,9],[6,[4,9]]]]
[[2,[[7,7],7]],[[5,8],[[9,3],[0,2]]]]
[[[[5,2],5],[8,[3,7]]],[[5,[7,5]],[4,4]]]
"""

EXAMPLES_EXPLODE = (
    ('[[[[[9,8],1],2],3],4]', '[[[[0,9],2],3],4]'),
    ('[7,[6,[5,[4,[3,2]]]]]', '[7,[6,[5,[7,0]]]]'),
    ('[[6,[5,[4,[3,2]]]],1]', '[[6,[5,[7,0]]],3]'),
    ('[[3,[2,[1,[7,3]]]],[6,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]'),  # noqa
    ('[[3,[2,[8,0]]],[9,[5,[4,[3,2]]]]]', '[[3,[2,[8,0]]],[9,[5,[7,0]]]]'),
    ('[[[[[4,3],4],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[7,[[8,4],9]]],[1,1]]'),  # noqa
    ('[[[[0,7],4],[7,[[8,4],9]]],[1,1]]', '[[[[0,7],4],[15,[0,13]]],[1,1]]')
)

EXAMPLES_SPLIT = (
    ('[15,[0,13]]', '[[7,8],[0,13]]'),
    ('[10,[0,13]]', '[[5,5],[0,13]]'),
    ('[11,[0,13]]', '[[5,6],[0,13]]'),
    ('[8,13]', '[8,[6,7]]'),
)

EXAMPLES_ADD = (
    (('[[[0,[4,5]],[0,0]],[[[4,5],[2,6]],[9,5]]]', '[7,[[[3,7],[4,3]],[[6,3],[8,8]]]]'), '[[[[4,0],[5,4]],[[7,7],[6,0]]],[[8,[7,7]],[[7,9],[5,0]]]]'),  # noqa


)

EXAMPLES_SUM = (
    (HOMEWORK_1, '[[[[1,1],[2,2]],[3,3]],[4,4]]'),  # noqa
    (HOMEWORK_2, '[[[[3,0],[5,3]],[4,4]],[5,5]]'),  # noqa
    (HOMEWORK_3, '[[[[5,0],[7,4]],[5,5]],[6,6]]'),  # noqa
    (HOMEWORK_4, '[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]'),  # noqa
    (HOMEWORK_5, '[[[[6,6],[7,6]],[[7,7],[7,0]]],[[[7,7],[7,7]],[[7,8],[9,9]]]]'),  # noqa
)

EXAMPLES_MAGNITUDE = (
    ('[9,1]', 29),
    ('[1,9]', 21),
    ('[[9,1],[1,9]]', 129),
    ('[[1,2],[[3,4],5]]', 143),
    ('[[[[0,7],4],[[7,8],[6,0]]],[8,1]]', 1384),
    ('[[[[1,1],[2,2]],[3,3]],[4,4]]', 445),
    ('[[[[3,0],[5,3]],[4,4]],[5,5]]', 791),
    ('[[[[5,0],[7,4]],[5,5]],[6,6]]', 1137),
    ('[[[[8,7],[7,7]],[[8,6],[7,7]]],[[[0,7],[6,6]],[8,7]]]', 3488),
)

EXAMPLES = (
    (HOMEWORK_5, 4140),
)

EXAMPLES_MAX = (
    (HOMEWORK_5, 3993),
)


@pytest.mark.parametrize('data,expected', EXAMPLES_EXPLODE)
def test_explode(data, expected):
    assert explode_expr(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_SPLIT)
def test_split(data, expected):
    assert split_expr(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_ADD)
def test_add(data, expected):
    assert add_expr(*data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_SUM)
def test_sum(data, expected):
    assert find_sum(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_MAGNITUDE)
def test_magnitude(data, expected):
    assert calc_magnitude(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES)
def test_solve(data, expected):
    assert solve(data) == expected


@pytest.mark.parametrize('data,expected', EXAMPLES_MAX)
def test_solve2(data, expected):
    assert solve2(data) == expected
