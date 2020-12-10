input1 = [16, 10, 15, 5, 1, 11, 7, 19, 6, 12, 4]
input2 = [28, 33, 18, 42, 31, 14, 46, 20, 48, 47, 24, 23, 49, 45, 19, 38, 39, 11, 1, 32, 25, 35, 8, 17, 7, 9, 4, 2, 34, 10, 3]  # noqa


def get_differences_array(input):
    data = [0] + sorted(input) + [max(input) + 3]
    result = {}
    data_len = len(data)
    for count, val in enumerate(data):
        if count < data_len - 1:
            num = data[count + 1] - val
            result.setdefault(num, 0)
            result[num] += 1
    return result


if __name__ =='__main__':

    # Part 1
    result_dict = get_differences_array(input1)
    result = result_dict[1] * result_dict[3]
    print('Test set 1: ', result)

    result_dict = get_differences_array(input2)
    result = result_dict[1] * result_dict[3]
    print('Test set 2: ', result)
