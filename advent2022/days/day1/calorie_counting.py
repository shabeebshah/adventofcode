# read input from file line by line until end of file
# sum each number you find until you find a blank line
# put running total into a list, keep track of max
# return max
import unittest


def calc_max_calories(file_name):
    elf_calories = []
    max_calories = -1

    with open(file_name) as calories_file:
        calories = 0
        for line in calories_file:
            if line.strip():
                calories += int(line)
            else:
                if calories > max_calories:
                    max_calories = calories
                elf_calories.append(calories)
                calories = 0

        if calories > max_calories:
            max_calories = calories
        elf_calories.append(calories)
    print(max_calories)
    return elf_calories


def calc_max_three_calories(elf_calories):
    elf_calories.sort()
    top_three_total = sum(elf_calories[-3:])
    print(top_three_total)
    return top_three_total


class CalorieCountingTest(unittest.TestCase):
    def test_prompt_one(self):
        self.assertEqual(calc_max_calories('prompt_calories.txt'), 24000)

    def test_prompt_two(self):
        self.assertEqual(calc_max_three_calories(calc_max_calories('prompt_calories.txt')), 45000)

    def test_part_one(self):
        self.assertEqual(calc_max_calories('calories.txt'), 69795)

    def test_part_two(self):
        self.assertTrue(calc_max_three_calories(calc_max_calories('calories.txt')))
