#https://adventofcode.com/2021/day/10
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import aoc_recipes




test_input="""
[({(<(())[]>[[{[]{<()<>>
[(()[<>])]({[<{<<[]>>(
{([(<{}[<>[]}>{[]{[(<()>
(((({<>}<{<{<>}{[]{[]{}
[[<[([]))<([[{}[[()]]]
[{[{({}]{}}([{[{{{}}([]
{<[[]]>}<{[{[{[]{()[[[]
[<(<(<(<{}))><([]([]()
<{([([[(<>()){}]>(<<{{
<{([{{}}[<[[[<>{}]]]>[]]
"""

SCORE_CORRUCT = {
    ")": 3,
    "]": 57,
    "}": 1197,
    ">": 25137,
    }
    
SCORE_INCOMPLE = {
    ")": 1,
    "]": 2,
    "}": 3,
    ">": 4,
    }

CHUNK_PAIRS = aoc_recipes.make_mirror_dict("() [] {} <>".split())

class CorructedChunk(Exception):
    def __init__(self, got, expected):
        self.got = got
        self.expected = expected


def parse(text:str) -> list[str]:
    """return a list of open chunsk that miss their closing parner"""
    open_chuck = []
    for c in text:
        if c in "([<{":
            open_chuck.append(c)
        elif c in ")]>}":
            if not open_chuck:
                raise ValueError(f"not opening for closing {c}")
            if CHUNK_PAIRS[c] == open_chuck[-1]:
                open_chuck.pop()
            else:
                raise CorructedChunk(c,CHUNK_PAIRS[open_chuck[-1]])
    open_chuck.reverse()
    return open_chuck


def process_data(data:str) -> Iterable[str]:
    """transform the raw data into a procesable form"""
    return ir.interesting_lines(data)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



