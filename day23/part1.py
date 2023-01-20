# https://adventofcode.com/2021/day/23
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import move, shortest_path_amphipod


def main(data:str) -> int:
    """part 1 of the puzzle """
    start = process_data(data)
    return shortest_path_amphipod(start)


def test() -> bool:
    return main(test_input) == 12521


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 18051
    pass












