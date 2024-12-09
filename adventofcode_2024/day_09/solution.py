"""Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9

"""

def data_gen(data):
    for i in data.strip():
        yield int(i)


def find_first_empty_position(disc, n):
    # print('HERE')
    while True:
        if disc[n] == '.':
            return n
        n += 1


def solve(data):
    disc = {}
    counter = 0
    id_counter = 0
    for e, i in enumerate(data_gen(data)):
        #print(e, i)
        j = i
        while j:
            if e % 2 == 0:
                disc[counter] = id_counter
            else:
                disc[counter] = '.'
            j -= 1
            counter += 1
        if e % 2:
            id_counter += 1
    #print(disc)
    #print(disc.values())


    position = 0
    counter -= 1
    while counter:
        v = disc[counter]
        if v != '.':
            position = find_first_empty_position(disc, position)
            #print('POSITION', position, counter, disc[position], disc[counter])
            #print(disc.values())
            if position <= counter:
                disc[position] = v
                disc[counter] = '.'
        counter -= 1

    #print(disc)
    #print(disc.values())

    # calculate checksum

    checksum = 0
    for k, v in disc.items():
        if v == '.':
            return checksum
        checksum += k * v

    return checksum



def solve2(data):
    disc = {}
    # id, ch, len
    counter = 0
    id_counter = 0
    for e, i in enumerate(data_gen(data)):
        if e % 2 == 0:
            v = id_counter
            id_counter += 1
        else:
            v = '.'
        disc[e] = (v, i)


    el_0 = Element(
        ch = data
    )


    id_counter = 0
    for e, i in enumerate(data_gen(data)):
        if e % 2 == 0:
            v = id_counter
            id_counter += 1
        else:
            v = '.'
        disc[e] = (v, i)


    print(disc)
    print(disc.values())



class Element:

    def __init__(self, ch, ch_len, left=None, right=None):
        self.ch = ch
        self.ch_len = ch_len
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.ch) * self.ch_len




if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
