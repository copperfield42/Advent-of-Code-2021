#https://adventofcode.com/2021/day/14
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import ipolymerization
from aoc_recipes import progress_bar
from collections import Counter
from functools_recipes import dual_reduce
from itertools import pairwise


class PolymerCount:

    def __init__(self, text:str):
        self.data = Counter(text)
        self.pairs = Counter(pairwise(text))
        
    def polymerization(self,pair_insertion:dict[tuple[str,str],str]):
        pairs = Counter()
        for pair,n in self.pairs.items():
            if pair in pair_insertion:
                a,b = pair
                c = pair_insertion[pair]
                pairs[(a,c)] += n
                pairs[(c,b)] += n
                self.data[c] += n
            else:
                pairs[pair] += n
        self.pairs = pairs


def main(data:str) -> int:
    """part 2 of the puzzle """
    base, rules = process_data(data)
    new_rules = {tuple(k):v for k,v in rules}
    polymer = PolymerCount(base)
    for _ in range(40):
        polymer.polymerization(new_rules)
    lc,mc = dual_reduce(polymer.data.values())
    return mc-lc


def test() -> bool:
    return main(test_input) == 2188189693529



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













