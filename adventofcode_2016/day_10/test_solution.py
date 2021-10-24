import pytest

from .solution import solve_bot, solve_outputs

EXAMPLES = (
    ("""value 5 goes to bot 2
bot 2 gives low to bot 1 and high to bot 0
value 3 goes to bot 1
bot 1 gives low to output 1 and high to bot 0
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 2""", (2, 5), 2),
    ("""value 7 goes to bot 1
value 8 goes to bot 1""", (7, 8), 1),
    ("""value 5 goes to bot 7
value 4 goes to bot 7""", (4, 5), 7),
    ("""value 1 goes to bot 99
value 2 goes to bot 99""", (1, 2), 99),
    ("""value 7 goes to bot 5
value 1 goes to bot 99
value 2 goes to bot 99""", (1, 2), 99),
    ("""value 1 goes to bot 99
value 7 goes to bot 5
value 2 goes to bot 99""", (1, 2), 99),
    ("""value 1 goes to bot 99
bot 0 gives low to output 2 and high to output 0
value 2 goes to bot 99""", (1, 2), 99),
    ("""value 100 goes to bot 5
value 10 goes to bot 5
value 1 goes to bot 3""", (10, 100), 5),
    ("""value 7 goes to bot 5
value 1 goes to bot 99
value 2 goes to bot 99
value 13 goes to bot 100""", (1, 2), 99),
    ("""value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 2
bot 1 gives low to bot 2 and high to output 0""", (1, 3), 2),
    ("""value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 3
value 4 goes to bot 3
bot 1 gives low to bot 2 and high to output 0
bot 3 gives low to output 7 and high to bot 2""", (1, 4), 2),
    ("""value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 3
value 4 goes to bot 4
bot 1 gives low to bot 3 and high to bot 4
bot 3 gives low to bot 2 and high to output 7
bot 4 gives low to output 8 and high to bot 2""", (1, 4), 2),
)

EXAMPLES_OUTPUTS = (
    ("""value 1 goes to bot 1
value 2 goes to bot 1
value 3 goes to bot 2
value 4 goes to bot 2
bot 1 gives low to output 1 and high to output 0
bot 2 gives low to bot 5 and high to output 7""", (0, 1, 7), 8),
)


@pytest.mark.parametrize('instructions,values,bot', EXAMPLES)
def test_solve_bot(instructions, values, bot):
    assert solve_bot(instructions, values) == bot


@pytest.mark.parametrize('instructions,outputs,expected', EXAMPLES_OUTPUTS)
def test_solve_outputs(instructions, outputs, expected):
    assert solve_outputs(instructions, outputs) == expected
