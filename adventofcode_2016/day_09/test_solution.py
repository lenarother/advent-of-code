import pytest

from .solution import decompress, decompress_v2, find_text_length

EXAMPLES = (
    ('ADVENT', 6),
    ('A(1x5)BC', 7),
    ('A(1x10)BC', 12),
    ('(3x3)XYZ', 9),
    ('A(2x2)BCD(2x2)EFG', 11),
    ('(6x1)(1x3)A', 6),
    ('X(8x2)(3x3)ABCY', 18),
    ('X(9x2)A(4x3)ABCY', 20),
)

EXAMPLES_WITH_MARKER = [
    ('ADVENT', 6),
    ('A(1x5)BC', 7),
    ('A(1x10)BC', 12),
    ('(3x3)XYZ', 9),
    ('(6x2)(3x1)A', 2),
    # ('X(9x2)A(4x3)ABCY', 24),
    ('X(8x2)(3x3)ABCY', 20),
    ('(27x12)(20x12)(13x14)(7x10)(1x12)A', 241920),
    ('(25x3)(3x3)ABC(2x3)XY(5x2)PQRSTX(18x9)(3x2)TWO(5x7)SEVEN', 445),
]


@pytest.mark.parametrize('compressed,length', EXAMPLES)
def test_find_length(compressed, length):
    assert find_text_length(compressed) == length


@pytest.mark.parametrize('compressed,length', EXAMPLES_WITH_MARKER)
def test_decompress(compressed, length):
    assert decompress(compressed) == length


@pytest.mark.parametrize('compressed,length', EXAMPLES_WITH_MARKER)
def test_decompress_v2(compressed, length):
    assert decompress_v2(compressed) == length
