#https://adventofcode.com/2021/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Probe, Point, astuple, calculate_min_x
from aoc_recipes import progress_bar
from itertools_recipes import consume



def main(data:str) -> int:
    """part 2 of the puzzle """
    target = process_data(data)
    M = max(astuple(target))
    m = min(astuple(target))
    mx = calculate_min_x( target.min_x )
    Mx = target.max_x+1
    print(f"Search space {m=} {M=}")
    print(f"Search space {mx=} {Mx=}")
    hits = 0
    for y in progress_bar(range(m,M),position=0):
        for x in progress_bar(range(mx,Mx),position=1,leave=False):
            v = Point(x,y)
            p = Probe(v,target)
            consume(p)
            hits += p.hit
    return hits


def test() -> bool:
    return main(test_input) == 112



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













