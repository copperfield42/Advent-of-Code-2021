#https://adventofcode.com/2021/day/14
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import ipolymerization
from collections import Counter
from functools_recipes import dual_reduce





def main(data:str, steps:int = 10) -> int:
    """part 1 of the puzzle """
    polymer, rules = process_data(data)
    new_rules = {tuple(k):v for k,v in rules}
    for _ in range(steps):
        polymer = ipolymerization(polymer, new_rules)
    count = Counter(polymer)
    lc,mc = dual_reduce(count.values())
    print(f"{mc=} {lc=}")
    return mc-lc    


def test() -> bool:
    return main(test_input) == 1588



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 2223
    












