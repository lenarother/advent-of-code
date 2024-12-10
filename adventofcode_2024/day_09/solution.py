"""Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9

"""

def data_gen(data):
    for i in data.strip():
        yield int(i)


def find_first_empty_location(disc, n):
    """First for a first available dot.

    Start looking from n, not from beginning.
    """
    while True:
        if disc[n] == '.':
            return n
        n += 1


def parse_data_to_dict(data):
    """Create disc map

    Parse data to a dictionary.
    disc[position] = partition_id or '.' (if empty)

    Contains one key for each disc position
    """
    disc = dict()
    disc_location = 0
    partition_id = 0
    for counter, partition_size in enumerate(data.strip()):
        is_occupied = counter % 2 == 0
        for _ in range(0, int(partition_size)):
            disc[disc_location] = partition_id if is_occupied else '.'
            disc_location += 1
        if is_occupied:
            partition_id += 1
    return disc


def move_data(disc):
    new_location = 0
    disc_location_from_end = len(disc) - 1
    while disc_location_from_end:
        partition_id = disc[disc_location_from_end]
        if partition_id != '.':
            new_location = find_first_empty_location(disc, new_location)
            if new_location <= disc_location_from_end:
                disc[new_location] = partition_id
                disc[disc_location_from_end] = '.'
        disc_location_from_end -= 1


def calculate_checksum(disc):
    checksum = 0
    for k, v in disc.items():
        if v == '.':
            return checksum
        checksum += k * v
    return checksum


def solve(data):
    disc = parse_data_to_dict(data)
    move_data(disc)
    return calculate_checksum(disc)


def parse_data_to_dict_2(data):
    """Create disc map.

    Parse data to a dictionary.
    disc[position] = (partition_id or '.', partition_size)

    Contains one key for each partition.
    Keys are not continous.
    """
    disc: dict[int, tuple[int|str, int]] = {}
    occupied_partition_locations: list[int] = []
    partition_id = 0
    disc_location = 0
    for counter, partition_size in enumerate(data_gen(data)):
        is_occupied = counter % 2 == 0
        if is_occupied:
            disc[disc_location] = (partition_id, partition_size)
            partition_id += 1
            occupied_partition_locations.append(disc_location)
        else:
            disc[disc_location] = ('.', partition_size)
        disc_location += partition_size
    return disc, occupied_partition_locations


def calculate_checksum_2(disc):
    checksum = 0
    for disc_location in disc:
        partition_id, partition_size = disc[disc_location]
        if partition_id != '.':
            for counter in range(0, partition_size):
                checksum += partition_id * (disc_location + counter)
    return checksum


def find_empty_location_2(disc, disc_location_from_end, partition_size):
    """First for a first available dot.

    Start looking from n, not from beginning.
    """
    empty_disc_location = None

    for disc_location_from_start in sorted(disc.keys()):
        tried_id, tried_size = disc[disc_location_from_start]

        if disc_location_from_start >= disc_location_from_end:
            empty_disc_location = None
            break
        elif tried_id == '.' and tried_size >= partition_size:
            empty_disc_location = disc_location_from_start
            break
        else:
            empty_disc_location = None
    return empty_disc_location


def solve2(data):
    disc, occupied_partition_locations = parse_data_to_dict_2(data)

    for disc_location_from_end in reversed(occupied_partition_locations):
        partition_id, partition_size = disc[disc_location_from_end]
        empty_disc_location = find_empty_location_2(
            disc, disc_location_from_end, partition_size
        )

        if empty_disc_location:
            disc.pop(disc_location_from_end)
            empty_location_id, empty_size = disc.pop(empty_disc_location)
            disc[empty_disc_location] = (partition_id, partition_size)
            if empty_size > partition_size:
                # smaller empty partition needs to be inserted
                new_size = empty_size - partition_size
                disc[empty_disc_location + partition_size] = ('.', new_size)

    return calculate_checksum_2(disc)


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
