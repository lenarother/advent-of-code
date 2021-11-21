import pytest

from .solution import count_valid_ips, support_ssl, support_tls

EXAMPLES = (
    ('abba[mnop]qrst', True),
    ('abcd[bddb]xyyx', False),
    ('aaaa[qwer]tyui', False),
    ('ioxxoj[asdfgh]zxcvbn', True),
    ('abba[qwer]tyui[bbbb]aaaa[abba]', False),
    ('abcbca', False),
)

EXAMPLES_SSL = (
    ('aba[bab]xyz', True),
    ('xyx[xyx]xyx', False),
    ('aaa[kek]eke', True),
    ('zazbz[bzb]cdb', True),
    ('cccbaba[bab]cdb', True),
)

EXAMPLES_LIST = (
    (['abcd[bddb]xyyx'], 0),
    (['abba[mnop]qrst'], 1),
    (['abba[mnop]qrst', 'ioxxoj[asdfgh]zxcvbn'], 2),
)


@pytest.mark.parametrize('ip,result', EXAMPLES)
def test_support_tls(ip, result):
    assert support_tls(ip) == result


@pytest.mark.parametrize('ip_list,result', EXAMPLES_LIST)
def test_count_valid_ips(ip_list, result):
    assert count_valid_ips(ip_list) == result


@pytest.mark.parametrize('ip,result', EXAMPLES_SSL)
def test_support_ssl(ip, result):
    assert support_ssl(ip) == result
