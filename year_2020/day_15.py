"""Day 15: Rambunctious Recitation

https://adventofcode.com/2020/day/15

"""

input1 = [0, 3, 6]  # 436

input2 = [1, 3, 2]  # 1
input3 = [2, 1, 3]  # 10
input4 = [1, 2, 3]  # 27
input5 = [2, 3, 1]  # 78
input6 = [3, 2, 1]  # 438
input7 = [3, 1, 2]  # 1836

input8 = [17, 1, 3, 16, 19, 0]


class Game:

    def __init__(self, initial_nums):
        self.nums = {}
        for counter, num in enumerate(initial_nums):
            self.nums[num] = [counter + 1]
        self.current_num = 0
        self.turn = len(initial_nums) + 1
        self.nums.setdefault(0, [])
        self.nums[0].append(self.turn)

    def play_turn(self):
        self.turn += 1

        if len(self.nums[self.current_num]) == 1:
            self.current_num = 0
        else:
            self.current_num = self.nums[self.current_num][-1] - self.nums[self.current_num][-2]

        self.nums.setdefault(self.current_num, [])
        self.nums[self.current_num].append(self.turn)

    def play(self, turns_num):
        while self.turn < turns_num:
            self.play_turn()
        return self.current_num


if __name__ =='__main__':

    # Part 1
    result = Game(input1).play(2020)
    print('Part 1 - Test set 1: ', result)

    assert Game(input2).play(2020) == 1
    assert Game(input3).play(2020) == 10
    assert Game(input4).play(2020) == 27
    assert Game(input5).play(2020) == 78
    assert Game(input6).play(2020) == 438
    assert Game(input7).play(2020) == 1836

    result = Game(input8).play(2020)
    print('Part 1 - Result: ', result)

    # Part 2
    result = Game(input8).play(30000000)
    print('Part 2 - Result: ', result)
