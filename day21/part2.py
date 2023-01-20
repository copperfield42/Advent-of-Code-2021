#https://adventofcode.com/2021/day/21
from __future__ import annotations

from collections import Counter
from functools import cache
from itertools import product

from aoc_utils import test_input, get_raw_data, process_data


diracDice = Counter(map(sum, product([1, 2, 3], repeat=3)))


@cache
def dirac_game(pos_p1: int, score_p1: int,  pos_p2: int, score_p2: int ):
    """ https://www.youtube.com/watch?v=rEyAbeV48tI """
    p1_wins = p2_wins = 0
    for roll, possibilities in diracDice.items():
        new_pos_p1 = ((pos_p1 + roll) % 10) or 10
        new_score_p1 = score_p1 + new_pos_p1
        if new_score_p1 >= 21:
            p1_wins += possibilities
        else:
            p2_wins_temp, p1_wins_temp = dirac_game(pos_p2, score_p2, new_pos_p1, new_score_p1)
            p1_wins += p1_wins_temp * possibilities
            p2_wins += p2_wins_temp * possibilities
    return p1_wins, p2_wins


def main(data: str) -> int:
    """part 2 of the puzzle """
    players = process_data(data)
    result = dirac_game(players[1], 0, players[2], 0)
    print(result)
    return max(result)


def test() -> bool:
    return main(test_input) == 444356092776315



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













