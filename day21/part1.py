#https://adventofcode.com/2021/day/21
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data, DiracDice


def main(data:str) -> int:
    """part 1 of the puzzle """
    game = DiracDice(process_data(data))
    rolls, players = game.play()
    score: int = min( x["score"] for x in players.values() )
    return rolls * score


def test() -> bool:
    return main(test_input) == 739785



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












