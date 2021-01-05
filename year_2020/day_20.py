"""Day 20: Jurassic Jigsaw

https://adventofcode.com/2020/day/20

"""

import re


class Tile:

    def __init__(self, id, initial_data):
        self.id = id
        self.initial_data = initial_data

        self.edges = self.set_edges(initial_data)

        self.data = None
        self.position = None
        self.is_border = None
        self.is_corner = None

    def set_edges(self, initial_data):
        initial_data_t_start = ''.join([x[0] for x in initial_data])
        initial_data_t_end = ''.join([x[-1] for x in initial_data])
        return {
            'T': initial_data[0],  # top
            'FT': initial_data[0][::-1],  # flipped top
            'B': initial_data[-1],  # bottom
            'FB': initial_data[-1][::-1],  # flipped bottom
            'L': initial_data_t_start,  # left
            'FL': initial_data_t_start[::-1],  # flipped left
            'R': initial_data_t_end,  # right
            'FR': initial_data_t_end[::-1],  # flipped right
        }

    def get_edge_orientation(self, edge):
        for k, v in self.edges.items():
            if v == edge:
                return k

    def orient(self, left):
        if left == 'L':
            self.data = self.initial_data
        elif left == 'R':
            self.data = [l[::-1] for l in self.initial_data]
        elif left == 'FL':
            self.data = self.initial_data[::-1]
        elif left == 'FR':
            self.data = [l[::-1] for l in self.initial_data][::-1]
        elif left == 'T':
            self.data = [''.join(x) for x in zip(*self.initial_data)]
        elif left == 'B':
            self.data = [''.join(x)[::-1] for x in zip(*self.initial_data)]
        elif left == 'FT':
            self.data = [''.join(x) for x in zip(*self.initial_data)][::-1]
        elif left == 'FB':
            self.data = [''.join(x)[::-1] for x in zip(*self.initial_data)][::-1]
        self.edges = self.set_edges(self.data)

    def find_neighbor_position(self, target):
        if target == 'T':
            return (self.position[0], self.position[1] - 1)
        if target == 'B':
            return (self.position[0], self.position[1] + 1)
        if target == 'R':
            return (self.position[0] + 1, self.position[1])
        if target == 'L':
            return (self.position[0] - 1, self.position[1])

    def get_relatve_left_orientation(self, edge_current_position, target):
        if target == 'L':
            return edge_current_position
        orientations = [
            ['L', 'T', 'R', 'B'],
            ['R', 'FT', 'L', 'FB'],
            ['FL', 'B', 'FR', 'T'],
            ['FR', 'FB', 'FL', 'FT'],
            ['FB', 'FR', 'FT', 'FL'],
            ['FT', 'R', 'FB', 'L'],
            ['B', 'FL', 'T', 'FR'],
            ['T', 'L', 'B', 'R'],
        ]
        if target == 'T':
            compare_position = 1
        elif target == 'R':
            compare_position = 2
        elif target == 'B':
            compare_position = 3
        for orientation in orientations:
            if orientation[compare_position] == edge_current_position:
                return orientation[0]

    def find_neighbor(self, matrix, tile_dict, edge_dict, my_edge_position, target_edge_position):
        position = self.find_neighbor_position(my_edge_position)
        if position in matrix.data:
            return True

        edge = self.edges[my_edge_position]
        ids = edge_dict[edge]

        if len(ids) == 1:
            if self.is_border:
                self.is_corner = True
            else:
                self.is_border = True
            return False

        neighbor_id = ids[0] if ids[0] != self.id else ids[1]
        neighbor_teil = tile_dict[neighbor_id]
        current_orientation = neighbor_teil.get_edge_orientation(edge) # R
        left_orientation = self.get_relatve_left_orientation(current_orientation, target_edge_position)
        neighbor_teil.orient(left=left_orientation)
        neighbor_teil.position = position
        matrix.add_tile(neighbor_teil, position)
        return True

    def find_neighbors(self, matrix, tile_dict, edge_dict):
        search = [('L', 'R'), ('R', 'L'), ('T', 'B'), ('B', 'T')]
        for my_edge_position, target_edge_position in search:
            self.find_neighbor(
                matrix,
                tile_dict,
                edge_dict,
                my_edge_position,
                target_edge_position
            )

    def crop(self):
        self.data = [l[1:-1] for l in self.data[1:-1]]


class Matrix:

    def __init__(self):
        self.data = {}
        self.picture = None
        self.text = None
        self.monster = None
        self.monster_hashes = None

    def add_tile(self, tile, position):
        self.data[position] = tile

    def set_picture(self):
        for teil in self.data.values():
            teil.crop()

        self.picture = []

        rows = {}
        for x, y in sorted(self.data.keys()):
            rows.setdefault(y, [])
            rows[y].append(self.data[(x, y)])

        for r in sorted(list(rows.keys())):
            for counter in range(len(self.data[(0, 0)].data)):
                l = ''.join([t.data[counter] for t in rows[r]])
                self.picture.append(l)

    def get_pictures(self):
        return {
            'L': self.picture,
            'R': [l[::-1] for l in self.picture],
            'FL': self.picture[::-1],
            'FR': [l[::-1] for l in self.picture][::-1],
            'T': [''.join(x) for x in zip(*self.picture)],
            'B': [''.join(x)[::-1] for x in zip(*self.picture)],
            'FT': [''.join(x) for x in zip(*self.picture)][::-1],
            'FB': [''.join(x)[::-1] for x in zip(*self.picture)][::-1],
        }

    def set_monster(self):
        monster = [
            '..................#.',
            '#....##....##....###',
            '.#..#..#..#..#..#...'
        ]
        between_len = len(self.picture[1]) - len(monster[0])
        self.monster = ('.' * between_len).join(monster)
        self.monster_hashes = [x.start() for x in re.finditer('#', self.monster)]

    def set_text(self):
        pictures = self.get_pictures()
        for p in pictures.values():
            text = ''.join(p)
            result = re.findall(self.monster, text)
            if len(result) > 0:
                self.text = text

    def find_monster_hashes(self, new_text=None, result=None, shift=0):
        if self.text is None:
            self.set_text()
        result = result or {}
        new_text = self.text if new_text is None else new_text
        search_result = re.search(self.monster, new_text)
        if search_result is None:
            return len(result)

        start = search_result.span()[0]
        result.update({(x + start + shift): True for x in self.monster_hashes})
        return self.find_monster_hashes(
            new_text=new_text[start + 1:],
            result=result,
            shift=shift + start + 1,
        )

    def calculate_water_roughness(self):
        monster_hashes = self.find_monster_hashes()
        all_hashes = self.text.count('#')
        return all_hashes - monster_hashes

    def get_corner_product(self):
        c1 = min(self.data.keys())
        c2 = max(self.data.keys())
        c3 = (c1[0], c2[1])
        c4 = (c2[0], c1[1])

        product = 1

        for c in [c1, c2, c3, c4]:
            tile = self.data[c]
            product = product * tile.id
        return product


def parse_input(filename):
    tile_dict = {}
    edge_dict = {}

    data = open(filename).read().strip().split('\n\n')
    for t in data:
        t = t.split('\n')
        tile = Tile(
            id=int(t[0].replace(':', '').replace('Tile ', '')),
            initial_data=t[1:],
        )
        tile_dict[tile.id] = tile
        for edge in tile.edges.values():
            edge_dict.setdefault(edge, [])
            edge_dict[edge].append(tile.id)

    return tile_dict, edge_dict


def _add_first_tile(matrix, tile, edge_dict):
    # Part 2
    if len(edge_dict[tile.edges['T']]) == 2:
        if len(edge_dict[tile.edges['R']]) == 2:
            tile.orient(left='L')
        else:
            tile.orient(left='FL')
    else:
        if len(edge_dict[tile.edges['R']]) == 2:
            tile.orient(left='R')
        else:
            tile.orient(left='FR')
    tile.position = (0, 0)
    matrix.add_tile(tile, (0, 0))


def get_matrix(filename):
    # Part 2
    tile_dict, edge_dict = parse_input(filename)
    m = Matrix()
    t = list(tile_dict.values())[0]
    _add_first_tile(m, t, edge_dict)
    while len(m.data) != len(tile_dict):
        for el in list(m.data.values()):
            el.find_neighbors(m, tile_dict, edge_dict)
    m.set_picture()
    m.set_monster()
    m.set_text()
    return m


if __name__ == '__main__':

    # Part 1
    m = get_matrix('inputdata/day-20-1.txt')
    result = m.get_corner_product()
    print('Part 1 - Test set 1: ', result)

    m = get_matrix('inputdata/day-20-2.txt')
    result = m.get_corner_product()
    print('Part 1 - Result: ', result)

    # Part 2
    m = get_matrix('inputdata/day-20-1.txt')
    result = m.calculate_water_roughness()
    print('Part 2 - Test set 1: ', result)

    m = get_matrix('inputdata/day-20-2.txt')
    result = m.calculate_water_roughness()
    print('Part 2 - Result: ', result)
