#https://adventofcode.com/2021/day/09
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import find_low_point


def main(data:str) -> int:
    """part 1 of the puzzle """
    heightmap = process_data(data)
    low = find_low_point(heightmap)
    return (heightmap[low]+1).sum()


def test() -> bool:
    return main(test_input) == 15



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # less than 702
    












