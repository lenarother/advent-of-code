import pytest

from .solution import get_checksum, get_data, get_odd_checksum, solve

EXAMPLES = (
    ('10000', 20, '01100'),
)

EXAMPLES_DATA = (
    ('1', 3, '100'),
    ('1', 2, '10'),
    ('0', 3, '001'),
    ('0', 2, '00'),
    ('11111', 11, '11111000000'),
    ('111100001010', 25, '1111000010100101011110000'),
)

EXAMPLES_CHECKSUM = (
    ('110010110100', '110101'),
    ('110101', '100'),
)

EXAMPLES_CHECKSUM_ODD = (
    ('110010110100', '100'),
)


@pytest.mark.parametrize('initial_state,disc_size,data', EXAMPLES_DATA)
def test_get_data(initial_state, disc_size, data):
    assert get_data(initial_state, disc_size) == data


@pytest.mark.parametrize('data,checksum', EXAMPLES_CHECKSUM)
def test_checksum(data, checksum):
    assert get_checksum(data) == checksum


@pytest.mark.parametrize('data,checksum', EXAMPLES_CHECKSUM_ODD)
def test_odd_checksum(data, checksum):
    assert get_odd_checksum(data) == checksum


@pytest.mark.parametrize('initial_state,disc_size,checksum', EXAMPLES)
def test_solve(initial_state, disc_size, checksum):
    assert solve(initial_state, disc_size) == checksum
