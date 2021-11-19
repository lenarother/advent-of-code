"""From Jens

https://www.reddit.com/r/dailyprogrammer/comments/onfehl/20210719_challenge_399_easy_letter_value_sum/

"""
from string import ascii_letters


def letter_sum(data):
    ch_value = {ch: (v + 1) for v, ch in enumerate(ascii_letters)}
    return sum([ch_value[ch] for ch in data])