"""Day 7: Internet Protocol Version 7

https://adventofcode.com/2016/day/7

An IP supports TLS if it has an Autonomous Bridge Bypass Annotation, or ABBA.
An ABBA is any four-character sequence which consists of a pair
of two different characters followed by the reverse of that pair,
such as xyyx or abba. However, the IP also must not have an ABBA
within any hypernet sequences, which are contained by square brackets.
"""
import re

PATTERN_ABBA = r'(\w)(\w)\2\1'
PATTERN_ABA = r'(\w)(\w)\1'
PATTERN_SPLIT_IP = r'\]?([a-z]+)\[?'


def get_ip_parts(ip, hypernet=True):
    return re.findall(PATTERN_SPLIT_IP, ip)[bool(hypernet)::2]


def has_abba(text):
    pattern = re.findall(PATTERN_ABBA, text)
    return any(map(lambda x: x == 2, map(len, map(set, pattern))))


def support_tls(ip):
    return (
        False if any(map(has_abba, get_ip_parts(ip, hypernet=True)))
        else has_abba(ip)
    )


def get_bab_iter(ip):
    already_occurred = {}

    for text in get_ip_parts(ip, hypernet=False):
        counter = 0

        while counter <= len(text) - 3:
            i = text[counter:]
            patterns = re.findall(PATTERN_ABA, i)

            for p in patterns:
                if p not in already_occurred and p[0] != p[1]:
                    already_occurred[p] = True
                    yield f'{p[1]}{p[0]}{p[1]}'

            counter += 1


def support_ssl(ip):
    return any([
        len(re.findall(bab, text))
        for text in get_ip_parts(ip, hypernet=True)
        for bab in get_bab_iter(ip)
    ])


def count_valid_ips(ip_list, alg=support_tls):
    return sum(map(alg, ip_list))


if __name__ == '__main__':
    f = open('input_data.txt')
    print(f'Example1: {count_valid_ips(f)}')
    f = open('input_data.txt')
    print(f'Example2: {count_valid_ips(f, support_ssl)}')
