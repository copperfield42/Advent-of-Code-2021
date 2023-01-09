#https://adventofcode.com/2021/day/20
from __future__ import annotations

from typing import Iterator, Iterable

import aoc_recipes
import itertools_recipes as ir
import numpy as np
from scipy.signal import convolve2d

test_input = """
..#.#..#####.#.#.#.###.##.....###.##.#..###.####..#####..#....#..#..##..###..######.###...####..#..#####..##..#.#####...##.#.#..#.##..#.#......#.###.######.###.####...#.##.##..#..#..#####.....#.#....###..#.##......#.....#..#..#..##..#...##.######.####.####.#.#...#.......#..#.#.#...####.##.#......#..#...##.#.##..#...##.#.##..###.#......#.#.......#.#.#.####.###.##...#.....####.#..#..#.##.#....##..#.####....##...##..#...#......#.#.......#.......##..####..#...#.#.#...##..#.#..###..#####........#..####......#..#

#..#.
#....
##..#
..#..
..###
"""

CON = np.array([[2**0,2**3,2**6],
                [2**1,2**4,2**7],
                [2**2,2**5,2**8]], dtype=int)


@np.vectorize
def apply_enhancenment(index: int, mask: int) -> bool:
    return bool((mask >> index) & 1)

def enhance_img(img: np.ndarray[bool,bool], enhanment: int, fillvalue:int=0) -> np.ndarray[bool,bool]:
    index = convolve2d(img, CON, mode="full", fillvalue=fillvalue)
    #return index
    return apply_enhancenment(index, enhanment)


def show(matrix: np.ndarray[bool,bool], fill: str=aoc_recipes.BLACK_char, empty: str= aoc_recipes.WHITE_char):
    X,Y = matrix.shape
    for y in range(Y):
        for x in range(X):
            print(fill if matrix[x,y] else empty, end="")
        print()


def process_data(data: str) -> tuple[int, np.ndarray[bool,bool]]:
    """transform the raw data into a procesable form"""
    lines = ir.interesting_lines(data)
    enhancement_raw = next(lines)
    img_raw = list(lines)
    Y = len(img_raw)
    X = len(img_raw[0])
    img = np.zeros((X,Y),dtype=bool)
    for y,line in enumerate(img_raw):
        for x,pixel in enumerate(line):
            img[x,y] = pixel == "#"
    enhancement = int( "".join("1" if c == "#" else "0" for c in reversed(enhancement_raw)), 2)
    return enhancement, img



def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



