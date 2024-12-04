"""Day 4: Ceres Search

https://adventofcode.com/2024/day/4

"""

def check_left_right(data):
    result = data.count("XMAS")
    result += data[::-1].count("XMAS")
    print('XXX', result)
    return result

def check_up_down(data):
    mylist = []
    for i in data.strip().split('\n'):
        mylist.append([j for j in i])
    data_t = "\n".join(map("".join, zip(*reversed(mylist))))

    result = data_t.count("XMAS")
    result += data_t[::-1].count("XMAS")
    print('XXX', result)
    return result

def check_diagonal(data):
    import numpy as np
    mylist = []
    for i in data.strip().split('\n'):
        mylist.append([j for j in i])
    a = np.array(mylist)

    diags = [a[::-1, :].diagonal(i) for i in range(-a.shape[0] + 1, a.shape[1])]

    # Now back to the original array to get the upper-left-to-lower-right diagonals,
    # starting from the right, so the range needed for shape (x,y) was y-1 to -x+1 descending.
    diags.extend(a.diagonal(i) for i in range(a.shape[1] - 1, -a.shape[0], -1))
    lists = [n.tolist() for n in diags]
    lists = [''.join(i) for i in lists]
    mystr = '\n'.join(lists)

    #print(mystr)
    result = mystr.count("XMAS")
    result += mystr[::-1].count("XMAS")
    print('XXX', result)
    return result


def solve(data):
    result = check_left_right(data)
    result += check_up_down(data)
    result += check_diagonal(data)
    print(result)
    return data


def solve2(data):
    result = check_left_right(data)
    result += check_up_down(data)
    result += check_diagonal(data)
    print(result)
    return data

if __name__ == '__main__':
    input_data = open('input_data.txt').read()
    result = solve(input_data)
    print(f'Example1: {result}')
