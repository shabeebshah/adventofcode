import unittest
from itertools import zip_longest


def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def map_value(item):
    mapped_value = 0
    if item.isupper():
        mapped_value = 27 + ord(item) % 65
    elif item.islower():
        mapped_value = 1 + ord(item) % 97

    return mapped_value


def find_item_priorities(filename):
    with open(filename) as rucksacks:
        sum_priorities = 0
        for rucksack in rucksacks:
            # Separate items
            rucksack_length = len(rucksack.strip())
            item_length = int(rucksack_length / 2)
            firstItem = rucksack[:item_length]
            second_item = rucksack[item_length:]

            # Find common items
            common_item = set(firstItem).intersection(second_item).pop()

            # Map item to priority
            mapped_value = map_value(common_item)

            # Sum priorities
            sum_priorities += mapped_value

        print(sum_priorities)
        return sum_priorities


def find_badges(filename):
    with open(filename) as rucksacks:
        sum_priorities = 0
        # Separate lines, 3 at a time
        for sack_group in grouper(rucksacks, 3, ''):
            # Find common item
            badge = set(sack_group[0].strip()).intersection(sack_group[1].strip(), sack_group[2].strip()).pop()

            # Map item to priority
            mapped_value = map_value(badge)

            # Sum priorities
            sum_priorities += mapped_value

    print(sum_priorities)
    return sum_priorities


class RucksackReorganization(unittest.TestCase):
    def test_prompt_one(self):
        self.assertEqual(find_item_priorities('prompt_sacks.txt'), 157)

    def test_part_one(self):
        self.assertTrue(find_item_priorities('rucksacks.txt'))

    def test_prompt_two(self):
        self.assertEqual(find_badges('prompt_sacks.txt'), 70)

    def test_part_two(self):
        self.assertEqual(find_badges('rucksacks.txt'), 2342)


