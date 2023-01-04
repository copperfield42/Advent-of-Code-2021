#https://adventofcode.com/2021/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import calculate_risk



def main(data:str) -> int:
    """part 1 of the puzzle """
    data = process_data(data)
    return calculate_risk(data)





def test() -> bool:
    return main(test_input) == 40



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) #













