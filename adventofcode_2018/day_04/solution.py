"""Day 4: Repose Record

https://adventofcode.com/2018/day/4

"""
import datetime
import re
from collections import Counter, defaultdict
from dataclasses import dataclass

from pydantic import validate_arguments

RECORD_BEGIN_SHIFT = (
    r'\[(?P<dt>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] '
    r'Guard #(?P<guard>\d+)'
)
RECORD_FALLS_ASLEEP = (
    r'\[(?P<dt>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] '
    r'falls asleep'
)
RECORD_WAKES_UP = (
    r'\[(?P<dt>\d{4}-\d{2}-\d{2} \d{2}:\d{2})\] '
    r'wakes up'
)

STATE_AWAKE = 0
STATE_ASLEEP = 1


@validate_arguments
@dataclass
class Record:
    dt: datetime.datetime
    guard: int = None
    is_asleep: bool = 0

    def __post_init__(self):
        self.clean()

    def clean(self):
        """Only midnight hour is relevant.

        If dt is not in midnight hour ->
        move to the next midnight hour.
        """
        if self.dt.hour != 0:
            self.dt += datetime.timedelta(days=1)
            self.dt = self.dt.replace(hour=0, minute=0)


def get_records_log(data):
    return sorted(data.strip().split('\n'))


def parse_record(record):
    for record_type, state in [
        (RECORD_BEGIN_SHIFT, STATE_AWAKE),
        (RECORD_FALLS_ASLEEP, STATE_ASLEEP),
        (RECORD_WAKES_UP, STATE_AWAKE),
    ]:
        record_match = re.match(record_type, record)
        if record_match:
            return Record(**record_match.groupdict(), is_asleep=state)


def collect_guards_asleep_minutes(records_log):
    guards_minutes = defaultdict(Counter)
    current_guard = None

    for i, j in zip(records_log[:-1], records_log[1:]):

        start_record = parse_record(i)
        stop_record = parse_record(j)

        if start_record.guard is not None:
            current_guard = start_record.guard

        if start_record.is_asleep:
            guards_minutes[current_guard] += Counter(range(
                start_record.dt.minute, stop_record.dt.minute
            ))
    return guards_minutes


def find_most_sleepy_guard(guards_data, strategy=sum):
    return max(
        guards_data.items(),
        key=lambda i: strategy(i[1].values())
    )[0]


def solve(data, strategy=sum):
    """Sneak in strategy 2.
        1. Find the most sleepy guard:
            * strategy 1:
                the guard that has the most minutes asleep.
            * strategy 2:
                the guard that is most frequently
                asleep on the same minute.
        2. Find minute that guard spend asleep the most.
        3. Return Guard-id * Minute-id
    """
    records_log = get_records_log(data)
    guards_data = collect_guards_asleep_minutes(records_log)

    most_sleepy_guard = find_most_sleepy_guard(guards_data, strategy)

    most_sleepy_guard_minutes = guards_data[most_sleepy_guard]
    most_sleepy_minute = max(
        most_sleepy_guard_minutes,
        key=most_sleepy_guard_minutes.get
    )
    return most_sleepy_guard * most_sleepy_minute


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data, strategy=sum)
    print(f'Example1: {result}')

    result = solve(input_data, strategy=max)
    print(f'Example2: {result}')
