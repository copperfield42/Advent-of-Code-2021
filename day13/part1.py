#https://adventofcode.com/2021/day/13
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import fold




def main(data:str) -> int:
    """part 1 of the puzzle """
    p,f = process_data(data)
    fp = fold(p,**(f[0]))
    return len(fp)


def test() -> bool:
    return main(test_input) == 17



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












