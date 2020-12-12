def get_input_list_from_file(filename):
    input = open(filename).readlines()
    return list(map(lambda x: x.strip(), input))
