def get_inpit_list_from_file(filename):
    input = open(filename).readlines()
    return list(map(lambda x: x.strip(), input))
