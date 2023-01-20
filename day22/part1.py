# https://adventofcode.com/2021/day/22
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Cuboid
from aoc_recipes import progress_bar




def main(data:str) -> int:
    """part 1 of the puzzle """
    on_cubes = set()
    cubo50 = Cuboid((-50, 50 + 1), (-50, 50 + 1), (-50, 50 + 1))
    work: Cuboid
    for work, val in progress_bar(process_data(data), position=0):
        pwork = progress_bar(work.sub_cuboid(cubo50), position=1, leave=False)
        if val:
            on_cubes.update(pwork)
        else:
            on_cubes.difference_update(pwork)
    return len(on_cubes)


def test() -> bool:
    return main(test_input) == 590784



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 606484
    












