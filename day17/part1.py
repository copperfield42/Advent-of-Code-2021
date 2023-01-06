#https://adventofcode.com/2021/day/17
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Point, Probe, calculate_min_x
from aoc_recipes import progress_bar



def main(data:str) -> int:
    """part 1 of the puzzle """
    target = process_data(data)
    M = max(target.center)
    m = min(target.center)
    max_y = -float("inf")
    mx = calculate_min_x( target.min_x ) 
    Mx = target.max_x+1
    print(f"Search space {m=} {M=}")
    print(f"Search space {mx=} {Mx=}")
    for y in progress_bar(range(m,M),position=0):
        for x in progress_bar(range(mx,Mx),position=1,leave=False):
            v = Point(x,y)
            p = Probe(v,target)
            mp = max(p, key=lambda t:t.y)
            if p.hit:
                max_y = max(max_y, mp.y)
    return max_y



def test() -> bool:
    return main(test_input) == 45

if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












