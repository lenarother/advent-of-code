import pytest

from .crack_password import find_code, find_sophisticated_code


@pytest.mark.slow
def test_find_code():
    assert find_code('abc') == '18f47a30'


@pytest.mark.slow
def test_find_sophisticated_code():
    assert find_sophisticated_code('abc') == '05ace8e3'
