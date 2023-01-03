#https://adventofcode.com/2021/day/13
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import fold, show





def main(data:str) -> int:
    """part 2 of the puzzle """
    p,f = process_data(data)
    for av in f:
        p = fold(p,**av)
    show(p)


def test() -> bool:
    return not main(test_input) 



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













