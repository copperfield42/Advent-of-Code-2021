# https://adventofcode.com/2021/day/23
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Amphipod, shortest_path_amphipod


def extend_amph(initial: Amphipod) -> Amphipod:
    extras = "DD", "CB", "BA", "AC"
    argv = list(initial)
    for i, add in enumerate(extras, 1):
        x, y = argv[i]
        argv[i] = x + add + y
    return Amphipod(*argv)


def main(data: str) -> int:
    """part 2 of the puzzle """
    start = extend_amph(process_data(data))
    return shortest_path_amphipod(start)


def test() -> bool:
    return main(test_input) == 44169


if __name__ == "__main__":
    assert test(), "fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data))  #















