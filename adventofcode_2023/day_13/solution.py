"""Day 13: Point of Incidence

https://adventofcode.com/2023/day/13

"""


def transpose(picture: str) -> str:
    picture = picture.strip().split('\n')
    return '\n'.join(["".join(x) for x in zip(*picture)])


def rows_from_up(picture: str) -> tuple[int, int]:
    """Calculate MIRROR-SIZE and RESULT for picture upper border.

    RESULT = 100 * rows up from reflection line
    Return MIRROR-SIZE, RESULT.
    """
    lines = picture.strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[0], range(len(lines))))

    for i in reversed(indices):
        candidate = lines[:i + 1]
        if candidate == candidate[::-1]:
            return len(candidate), (len(candidate) // 2) * 100
    return 0, 0


def rows_from_down(picture: str) -> tuple[int, int]:
    """Calculate MIRROR-SIZE and RESULT for picture lower border.

    RESULT = 100 * rows up from reflection line
    Return MIRROR-SIZE, RESULT.
    """
    lines = picture.strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[-1], range(len(lines))))

    for i in indices:
        candidate = lines[i:]
        if candidate == candidate[::-1]:
            return len(candidate), ((len(lines) - len(candidate)) + len(candidate) // 2) * 100
    return 0, 0


def columns_from_left(picture: str) -> tuple[int, int]:
    """Calculate MIRROR-SIZE and RESULT for picture left border.

    RESULT = rows left to reflection line
    Return MIRROR-SIZE, RESULT.
    """
    lines = transpose(picture).strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[0], range(len(lines))))

    for i in reversed(indices):
        candidate = lines[:i + 1]
        if candidate == candidate[::-1]:
            return len(candidate), (len(candidate) // 2)
    return 0, 0


def columns_from_right(picture: str) -> tuple[int, int]:
    """Calculate MIRROR-SIZE and RESULT for picture right border.

    RESULT = rows left to reflection line
    Return MIRROR-SIZE, RESULT.
    """
    lines = transpose(picture).strip().split('\n')
    indices = list(filter(lambda i: lines[i] == lines[-1], range(len(lines))))

    for i in indices:
        candidate = lines[i:]
        if candidate == candidate[::-1]:
            return len(candidate), ((len(lines) - len(candidate)) + len(candidate) // 2)
    return 0, 0


def find_mirror(picture: str) -> int:
    size = 0
    x = 0

    to_check = [
        rows_from_up,
        rows_from_down,
        columns_from_left,
        columns_from_right
    ]

    for f in to_check:
        n_size, n_x = f(picture)
        if n_size > size:
            size, x = n_size, n_x

    return x


def solve(data: str) -> int:
    return sum(find_mirror(picture) for picture in data.split('\n\n'))


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')
