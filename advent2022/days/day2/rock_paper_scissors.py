# A B C (1, 2, 3)
# X Y Z (1, 2, 3)
# L - 0, D - 3, W - 6
import unittest


def calc_game_score(filename):
    # read line, split strings, calculate via score map per round, sum and return
    score = 0
    # move_one = {'X': 1, 'Y': 2, 'Z': 3}
    # scoring_one = {'A': {'X': 3, 'Y': 6, 'Z': 0},
    #            'B': {'X': 0, 'Y': 3, 'Z': 6},
    #            'C': {'X': 6, 'Y': 0, 'Z': 3}}
    scoring_two = {'X': 0, 'Y': 3, 'Z': 6}
    move_two = {'X': {'A': 3, 'B': 1, 'C': 2},
                'Y': {'A': 1, 'B': 2, 'C': 3},
                'Z': {'A': 2, 'B': 3, 'C': 1}}

    with open(filename) as strategy_guide:
        for match in strategy_guide:
            moves = match.strip().split(' ')
            player_one = moves[0]
            player_two = moves[1]

            score += scoring_two[player_two] + move_two[player_two][player_one]

    print(score)
    return score


class RockPaperScissorsTest(unittest.TestCase):
    def test_prompt_one(self):
        self.assertEqual(calc_game_score('prompt_guide.txt'), 15)

    def test_prompt_two(self):
        self.assertEqual(calc_game_score('prompt_guide.txt'), 12)

    def test_part_one(self):
        self.assertEqual(calc_game_score('strategy_guide.txt'), 10816)

    def test_part_two(self):
        self.assertTrue(calc_game_score('strategy_guide.txt'), 11657)
