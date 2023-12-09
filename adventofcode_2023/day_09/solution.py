"""Day 9: Mirage Maintenance

https://adventofcode.com/2023/day/9

"""


class Row:

    def __init__(self, values):
        self.values = self.parse(values)
        self.rows = [self.values]

    def __str__(self):
        return f"{self.values}"

    @staticmethod
    def parse(values: str) -> list[int]:
        return [int(i) for i in values.split()]

    def get_new_row(self) -> list[int]:
        return [
            (y - x)
            for x, y in zip(self.rows[-1][0:-1], self.rows[-1][1:])
        ]

    def is_complete(self) -> bool:
        return all([i == 0 for i in self.rows[-1]])

    def add_rows(self):
        while not self.is_complete():
            self.rows.append(self.get_new_row())

    def extrapolate(self) -> int:
        self.rows[-1].append(0)
        for i in range(len(self.rows) - 1, 0, -1):
            last = self.rows[i][-1]
            previous = self.rows[i-1][-1]
            new_el = previous + last
            self.rows[i-1].append(new_el)
        return self.rows[0][-1]

    def history(self) -> int:
        self.rows[-1].insert(0, 0)
        for i in range(len(self.rows) - 1, 0, -1):
            last = self.rows[i][0]
            previous = self.rows[i-1][0]
            new_el = previous - last
            self.rows[i-1].insert(0, new_el)
        return self.rows[0][0]


def solve(data: str) -> int:
    rows = [Row(line) for line in data.split('\n')]
    counter = 0
    for row in rows:
        row.add_rows()
        counter += row.extrapolate()
    return counter


def solve_2(data: str) -> int:
    rows = [Row(line) for line in data.split('\n')]
    counter = 0
    for row in rows:
        row.add_rows()
        counter += row.history()
    return counter


if __name__ == '__main__':
    input_data = open('input_data.txt').read()

    result = solve(input_data)
    print(f'Example1: {result}')

    result = solve_2(input_data)
    print(f'Example1: {result}')
