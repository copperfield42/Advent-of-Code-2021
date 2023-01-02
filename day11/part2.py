#https://adventofcode.com/2021/day/11
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import light_cycle
from itertools import count



def main(data:str) -> int:
    """part 2 of the puzzle """
    energy = process_data(data)
    for i in count(1):
        energy = light_cycle(energy)
        if (energy==0).all():
            return i
    


def test() -> bool:
    return main(test_input) == 195



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













