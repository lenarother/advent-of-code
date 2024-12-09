"""Day 9: Disk Fragmenter

https://adventofcode.com/2024/day/9

"""

def data_gen(data):
    for i in data.strip():
        yield int(i)


def find_first_empty_position(disc, n):
    """First for a first available dot.

    Start looking from n, not from beginning.
    """
    while True:
        if disc[n] == '.':
            return n
        n += 1

def parse_data_to_dict(data):
    disc = dict()

    for counter, partition in enumerate(data.strip()):
        for _ in range(0, int(partition)):
            pass

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

    position = 0
    counter -= 1
    while counter:
        v = disc[counter]
        if v != '.':
            position = find_first_empty_position(disc, position)
            if position <= counter:
                disc[position] = v
                disc[counter] = '.'
        counter -= 1

    # calculate checksum
    checksum = 0
    for k, v in disc.items():
        if v == '.':
            return checksum
        checksum += k * v

    return checksum



def solve2(data):
    disc = {}
    # id, len
    counter = 0
    id_counter = 0
    myk = 0
    all_num_keys = []
    for e, i in enumerate(data_gen(data)):
        if e % 2 == 0:
            v = id_counter
            id_counter += 1
            all_num_keys.append(myk)
        else:
            v = '.'
        disc[myk] = (v, i)
        myk += i

    for i in reversed(all_num_keys):
        # print(i, disc[i])
        myn, myval = disc[i]
        target_k = None
        for n  in sorted(disc.keys()):
            val = disc[n]
            if n >= i:
                target_k = None
                break
            elif val[0] == '.' and val[1] >= myval:
                target_k = n
                break
            else:
                target_k = None
        # print(target_k)
        if target_k:
            disc.pop(i)
            foo_val = disc.pop(target_k)
            disc[target_k] = (myn, myval)
            if foo_val[1] > myval:
                leng = foo_val[1] - myval
                disc[target_k + leng + 1] = ('.', leng)


    # calculate checksum

    checksum = 0
    for k, v in disc.items():
        if v[0] != '.':
            x = v[1] #len
            c = 0
            while x:
                checksum += v[0] * (k + c)
                x -= 1
                c += 1

    #print(checksum)
    #print(disc)
    return checksum


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

    result = solve2(input_data)
    print(f'Example2: {result}')