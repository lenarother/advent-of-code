"""Day 2: Red-Nosed Reports

https://adventofcode.com/2024/day/2

"""


def parse_data(data):
    """
    Covers string input into list of losts.

    Args:
    Multiple line string with two numbers in each row.
        7 6 4 2 1
        1 2 7 8 9
    Returns:
        [[7, 6, 4, 2, 1], [1, 2, 7, 8, 9]]
    """
    reports = []
    for row in data.strip().split('\n'):
        reports.append([int(i) for i in row.split()])
    return reports


def solve(data):
    reports = parse_data(data)
    return sum([check_report(report) for report in reports])


def solve2(data):
    reports = parse_data(data)
    return sum([check_report_2(report) for report in reports])


def check_report(report):
    report_sorted = sorted(report)
    report_sorted_reversed = sorted(report, reverse=True)
    if not (report == report_sorted or report == report_sorted_reversed):
        return 0
    previous = report[0]
    for level in report[1:]:
        if not abs(previous - level) in [1, 2, 3]:
            return 0
        previous = level
    return 1


def check_report_2(report):
    if check_report(report):
        return 1
    for i in range(len(report)):
        new_report = report.copy()
        del (new_report[i])
        if check_report(new_report):
            return 1
    return 0


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve2(input_data)
    print(f'Example2: {result}')
