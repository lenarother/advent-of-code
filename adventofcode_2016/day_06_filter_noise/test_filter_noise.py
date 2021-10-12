import pytest

from .filter_noise import filter_modified_noise, filter_noise

EXAMPLES = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('c\nc', 'c'),
    ('b\na\na', 'a'),
    ('cd\ncb\nab', 'cb'),
    ("""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""", 'easter'),
)

EXAMPLES_MODIFIED = (
    ('a', 'a'),
    ('b', 'b'),
    ('c', 'c'),
    ('c\nc', 'c'),
    ('b\na\na', 'b'),
    ('cd\ncb\nab', 'ad'),
    ("""eedadn
drvtee
eandsr
raavrd
atevrs
tsrnev
sdttsa
rasrtv
nssdts
ntnada
svetve
tesnvt
vntsnd
vrdear
dvrsen
enarar""", 'advent'),
)


@pytest.mark.parametrize('noise,result', EXAMPLES)
def test_filter_noise(noise, result):
    assert filter_noise(noise) == result


@pytest.mark.parametrize('noise,result', EXAMPLES_MODIFIED)
def test_filter_modified_noise(noise, result):
    assert filter_modified_noise(noise) == result
