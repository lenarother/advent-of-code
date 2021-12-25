"""Day 25: Sea Cucumber

https://adventofcode.com/2021/day/25

"""


class Cucumbers:

    def __init__(self, data=None):
        self.data = {}
        self.len_x = None
        self.len_y = None
        if data:
            self.parse(data)

    def __repr__(self):
        repr = ''
        for y in range(self.len_y):
            for x in range(self.len_x):
                repr += self.data[(x, y)]
            repr += '\n'
        return repr

    def __iter__(self):
        for y in range(self.len_y):
            for x in range(self.len_x):
                yield x, y

    def parse(self, data):
        for y, row in enumerate(data.strip().split('\n')):
            for x, v in enumerate(row):
                self.data[x, y] = v
        self.len_x = x + 1
        self.len_y = y + 1

    def get_adj_position(self, pos):
        x, y = pos
        if self.data[pos] == 'v':
            return x, (y + 1) % self.len_y
        if self.data[pos] == '>':
            return (x + 1) % self.len_x, y

    def collect_moves_for_type(self, c_type):
        moves = []
        for p in self:
            if self.data[p] == c_type:
                adj_p = self.get_adj_position(p)
                if self.data[adj_p] == '.':
                    moves.append((p, adj_p))
        return moves

    def move_type(self, c_type):
        to_move = self.collect_moves_for_type(c_type)
        for p_current, p_target in to_move:
            self.data[p_target] = self.data[p_current]
            self.data[p_current] = '.'
        return len(to_move)

    def step(self):
        moved = self.move_type('>')
        moved += self.move_type('v')
        return moved

    def simulate(self):
        steps = 1
        while 1:
            moved = self.step()
            if moved == 0:
                return steps
            steps += 1


def solve(data):
    cucumbers = Cucumbers(data)
    return cucumbers.simulate()


if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
