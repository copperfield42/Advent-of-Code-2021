#https://adventofcode.com/2021/day/11
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy
from scipy.signal import convolve2d



test_input="""
5483143223
2745854711
5264556173
6141336146
6357385478
4167524645
2176841721
6882881134
4846848554
5283751526
"""

test_input_2 = """
11111
19991
19191
19991
11111
"""

CON = numpy.array( [ [1,1,1],
                     [1,0,1],
                     [1,1,1], ], dtype=int)

def light_cycle(energy:numpy.ndarray[int,int]) -> numpy.ndarray[int,int]:
    new = energy + 1
    mask = new>9
    light_up = mask
    while mask.any():
        con = convolve2d(mask,CON,mode="same")
        new = new + con
        mask = (new>9)^light_up
        light_up |= mask
    new[light_up] = 0
    return new


def process_data(data:str) -> numpy.ndarray[int,int]:
    """transform the raw data into a procesable form"""
    return numpy.array([list(map(int,line)) for line in ir.interesting_lines(data)], dtype=int)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




