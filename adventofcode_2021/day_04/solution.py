"""Day 4: Giant Squid

https://adventofcode.com/2021/day/4

"""


class Board:

    def __init__(self, data):
        self.current_n = None
        self.num_pos = {}
        self.pos_num = {}
        self.num_marked = {}
        self.row_marked_count = {}
        self.col_marked_count = {}
        self.parse(data)

    def parse(self, data):
        for y, l in enumerate(data.strip().split('\n')):
            for x, n in enumerate(l.split()):
                n = n.strip()
                if n:
                    self.pos_num[(x, y)] = int(n)
                    self.num_pos[int(n)] = (x, y)
                    self.num_marked[int(n)] = 0

    def mark(self, n):
        self.current_n = n
        if n in self.num_marked:
            self.num_marked[n] = 1
            x, y = self.num_pos[n]
            self.row_marked_count.setdefault(y, 0)
            self.row_marked_count[y] += 1
            self.col_marked_count.setdefault(x, 0)
            self.col_marked_count[x] += 1
            return True
        return False

    def is_winner(self):
        return (
            5 in self.row_marked_count.values() or
            5 in self.col_marked_count.values()
        )

    def win(self):
        return self.current_n * sum([
            k for k, v in self.num_marked.items()
            if v == 0
        ])


class Bingo:

    def __init__(self, data):
        self.boards = {}
        self.nums = []
        self.parse_data(data)

    def __len__(self):
        return len(self.boards)

    def parse_data(self, data):
        data = data.strip().split('\n\n')
        self.nums = map(int, data[0].split(','))
        for c, b in enumerate(data[1:]):
            self.boards[c] = Board(b)

    def call_num(self, n):
        for b in self.boards.values():
            b.mark(n)

    def get_winner(self):
        for b in self.boards.values():
            if b.is_winner():
                return b.win()
        return None

    def remove_winners(self):
        to_remove = []
        for k, v in self.boards.items():
            if v.is_winner():
                to_remove.append(k)
        for n in to_remove:
            if len(self) > 1:
                del self.boards[n]

    def play(self):
        for n in self.nums:
            self.call_num(n)
            winner = self.get_winner()
            if winner:
                return winner
        return 0

    def play2(self):
        for n in self.nums:
            self.call_num(n)
            self.remove_winners()
            if len(self) == 1:
                b = list(self.boards.values())[0]
                if b.is_winner():
                    return b.win()
        return 0


def solve(data):
    return Bingo(data).play()


def solve2(data):
    return Bingo(data).play2()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')

    input_data = open('input_data.txt').read()
    result = solve2(input_data)
    print(f'Example2: {result}')
