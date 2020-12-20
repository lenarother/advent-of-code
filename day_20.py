"""Day 20

https://adventofcode.com/2020/day/20

"""

def add_edge(result, edge, id):
    # Part 1
    if edge in result:
        result.pop(edge)
    else:
        result[edge] = id

def parse_input(filename):
    # Part 1
    data_dict = {}
    result = {}

    data = open(filename).read().strip().split('\n\n')
    for tile in data:
        tile = tile.split('\n')
        id = int(tile[0].replace(':', '').replace('Tile ', ''))
        teil_data = tile[1:]
        data_dict[id] = teil_data

        # Edges
        add_edge(result, teil_data[0], id)
        add_edge(result, teil_data[0][::-1], id)
        add_edge(result, teil_data[-1], id)
        add_edge(result, teil_data[-1][::-1], id)
        teil_data_t_start = ''.join([x[0] for x in teil_data])
        add_edge(result, teil_data_t_start, id)
        add_edge(result, teil_data_t_start[::-1], id)
        teil_data_t_end = ''.join([x[-1] for x in teil_data])
        add_edge(result, teil_data_t_end, id)
        add_edge(result, teil_data_t_end[::-1], id)

    return data_dict, result


def get_corners_product(filename):
    data, result = parse_input(filename)
    ids = {}
    for k, v in result.items():
        ids.setdefault(v, 0)
        ids[v] += 1

    max_v = max(list(ids.values()))
    product = 1
    for id, v in ids.items():
        if v == max_v:
            product = product * id

    return product


if __name__ =='__main__':

    # Part 1
    result = get_corners_product('inputdata/day-20-1.txt')
    print('Part 1 - Test set 1: ', result)

    result = get_corners_product('inputdata/day-20-2.txt')
    print('Part 1 - Result: ', result)
