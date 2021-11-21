import pytest

from .solution import count_pixels, display

EXAMPLES = (
    (
        ['rect 1x1'],
        '#....................'
    ),
    (
        ['rect 3x2'],
        '###....###...........'
    ),
    (
        ['rect 1x3'],
        '#......#......#......'
    ),
    (
        ['rect 1x3'],
        '#......#......#......'
    ),
    (
        ['rect 3x1', 'rect 2x2', 'rect 1x3'],
        '###....##.....#......'
    ),
    (
        ['rect 3x2', 'rotate column x=1 by 1'],
        '#.#....###.....#.....'
    ),
    (
        ['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4'],
        '....#.####.....#.....'
    ),
    (
        ['rect 7x3'],
        '#####################'
    ),
    (
        ['rect 1x1', 'rotate column x=0 by 3'],
        '#....................'
    ),
    (
        ['rect 1x1', 'rotate row y=0 by 7'],
        '#....................'
    ),
    (
        [
            'rect 3x2',
            'rotate column x=1 by 1',
            'rotate row y=0 by 4',
            'rotate column x=1 by 1',
        ],
        '.#..#.##.#.....#.....',
    ),
)

EXAMPLES_COUNT = (
    (['rect 1x1'], 1),
    (['rect 3x2', 'rotate column x=1 by 1', 'rotate row y=0 by 4'], 6),
)


@pytest.mark.parametrize('instructions,screen', EXAMPLES)
def test_display(instructions, screen):
    assert display(instructions) == screen


@pytest.mark.parametrize('instructions,count', EXAMPLES_COUNT)
def test_count_pixels(instructions, count):
    assert count_pixels(instructions) == count
