#https://adventofcode.com/2021/day/09
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import find_low_point
from aoc_recipes import where, make_vecinos, is_valid, Point
from math import prod
from collections import deque


def basin(coord:tuple[int,int], matrix:numpy.ndarray[int,int]) -> int:
    points = set()
    pen = deque([Point(*coord)])
    while pen:
        p = pen.pop()
        points.add(p)
        for np in make_vecinos(p,lambda x:is_valid(x,matrix.shape) and matrix[x]<9):
            if np not in points:
                pen.append(np)
    return len(points)
    

def main(data:str) -> int:
    """part 2 of the puzzle """
    heightmap = process_data(data)
    low = find_low_point(heightmap)
    basins = sorted( basin(p,heightmap) for p in where(low))
    result = basins[-3:]
    print("the number of low points is",low.sum(), "and the 3 bigest basins are", result)
    return prod(result)

def test() -> bool:
    return main(test_input) == 1134



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













