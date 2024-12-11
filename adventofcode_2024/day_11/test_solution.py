import pytest

from .solution import solve, solve_n, solve_list

EXAMPLES = (
    #("0 1 10 99 999", 1, 7),
    #("125 17", 1, 3),
    #("125 17", 6, 22),
    #("125 17", 6, 22),

    ("125 17", 25, 55312),
)#


@pytest.mark.parametrize('data, iterations, expected', EXAMPLES)
def test_solve(data, iterations, expected):
    assert solve(data, iterations) == expected


@pytest.mark.parametrize(
    'data, iterations, expected_len, expected_nums',
    (
        (["0"], 1, 1, ["1"]),
        (["0"], 2, 1, ["2024"]),
        (["0"], 4, 4, ["2", "0", "2", "4"]),
        (["0", "1"], 1, 2, ["1", "2024"]),
        (["0", "1"], 2, 3, ["2024", "20", "24"]),
        (["0", "1"], 3, 6, ["20", "24", "2", "0", "2", "4"]),
        (["125", "17"], 1, 3, ["253000", "1", "7"]),
        (["125", "17"], 2, 4, ["253", "0", "2024", "14168"]),
        (["125", "17"], 6, 22, ["2097446912", "14168", "4048", "2", "0", "2", "4", "40", "48", "2024", "40", "48", "80", "96", "2", "8", "6", "7", "6", "0", "3", "2"]),
        #("0", 7, 14, ["4", "0", "4", "8", "20", "24", "4", "0", "4", "8", "8", "0", "9", "6"]),
        #(["0"], 25, 14, ["4", "0", "4", "8", "20", "24", "4", "0", "4", "8", "8", "0", "9", "6"]),
    )

)
def test_solve_list(data, iterations, expected_len, expected_nums):
    assert solve_list(data, iterations, {}) == (expected_len, expected_nums)


@pytest.mark.parametrize(
    'data, iterations, expected_len, expected_nums',
    (
            #("0", 1, 1, ["1"]),
            ##("1", 1, 1, ["2024"]),
            #("0", 4, 4, ["2", "0", "2", "4"]),
            #("0", 7, 14, ["4", "0", "4", "8", "20", "24", "4", "0", "4", "8", "8", "0", "9", "6"]),
            ("0", 25, 14, ["4", "0", "4", "8", "20", "24", "4", "0", "4", "8", "8", "0", "9", "6"]),
    )

)
def test_solve_n(data, iterations, expected_len, expected_nums):
    return
    # print(solve_n(data, iterations, {}))
    assert solve_n(data, iterations, {}) == (expected_len, expected_nums)


['2097446912', '14168', '4048', '2', '0', '2', '4', '40', '48', '2024', '40', '48', '80', '96', '2', '8', '6', '7', '6', '0', '3', '2']
['2097446912', '14168', '4048', '2', '0', '2', '2', '40', '48', '2024', '40', '48', '80', '96', '2', '8', '6', '7', '6', '0', '3', '2']
