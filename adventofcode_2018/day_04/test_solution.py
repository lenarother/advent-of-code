import pytest

from .solution import (
    STATE_ASLEEP,
    STATE_AWAKE,
    Record,
    get_records_log,
    parse_record,
    solve,
)

DATA = """
[1518-11-01 00:05] falls asleep
[1518-11-05 00:45] falls asleep
[1518-11-01 00:30] falls asleep
[1518-11-02 00:40] falls asleep
[1518-11-03 00:24] falls asleep
[1518-11-04 00:36] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:55] wakes up
[1518-11-02 00:50] wakes up
[1518-11-05 00:55] wakes up
[1518-11-03 00:29] wakes up
[1518-11-04 00:46] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-05 00:03] Guard #99 begins shift
"""

DATA_SORTED = """
[1518-11-01 00:00] Guard #10 begins shift
[1518-11-01 00:05] falls asleep
[1518-11-01 00:25] wakes up
[1518-11-01 00:30] falls asleep
[1518-11-01 00:55] wakes up
[1518-11-01 23:58] Guard #99 begins shift
[1518-11-02 00:40] falls asleep
[1518-11-02 00:50] wakes up
[1518-11-03 00:05] Guard #10 begins shift
[1518-11-03 00:24] falls asleep
[1518-11-03 00:29] wakes up
[1518-11-04 00:02] Guard #99 begins shift
[1518-11-04 00:36] falls asleep
[1518-11-04 00:46] wakes up
[1518-11-05 00:03] Guard #99 begins shift
[1518-11-05 00:45] falls asleep
[1518-11-05 00:55] wakes up
"""


def test_get_records_log():
    records_log = get_records_log(DATA.strip())
    assert '\n'.join(records_log) == DATA_SORTED.strip()


@pytest.mark.parametrize(
    'record, expected',
    [
        (
            '[1518-11-01 00:00] Guard #10 begins shift',
            Record(dt='1518-11-01 00:00', guard=10, is_asleep=STATE_AWAKE)
        ),
        (
            '[1518-11-01 00:05] falls asleep',
            Record(dt='1518-11-01 00:05', is_asleep=STATE_ASLEEP)
        ),
        (
            '[1518-11-01 00:25] wakes up',
            Record(dt='1518-11-01 00:25', is_asleep=STATE_AWAKE)
        ),
        (
            '[1518-11-01 23:58] Guard #99 begins shift',
            Record(dt='1518-11-02 00:00', guard=99, is_asleep=STATE_AWAKE)
        ),
    ]
)
def test_parse_record(record, expected):
    assert parse_record(record) == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        (DATA, 240),
        (DATA_SORTED, 240),
    ]
)
def test_solve(data, expected):
    assert solve(data, strategy=sum) == expected


@pytest.mark.parametrize(
    'data, expected',
    [
        (DATA, 4455),
        (DATA_SORTED, 4455),
    ]
)
def test_solve2(data, expected):
    assert solve(data, strategy=max) == expected
