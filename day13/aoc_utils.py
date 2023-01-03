#https://adventofcode.com/2021/day/13
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from ast import literal_eval
from aoc_recipes import Point, BLACK_char, WHITE_char
from functools_recipes import dual_reduce



test_input="""
6,10
0,14
9,10
0,3
10,4
4,11
6,0
6,12
4,1
0,13
10,12
3,4
3,0
8,4
1,10
2,14
8,10
9,0

fold along y=7
fold along x=5
"""


def fold(points:Iterable[Point], axis:str, value:int) -> set[Points]:
    eje = Point(0,0)
    eje = eje._replace( **{axis:value} )
    result = set()
    for p in points:
        if getattr(p,axis) > value:
            p = p - eje._replace(**{axis:getattr((p-eje)*2,axis)})
        result.add(p)
    return result


def show(points:set[Point]):
    min_x,max_x = dual_reduce(p.x for p in points)
    min_y,max_y = dual_reduce(p.y for p in points)
    for y in range(min_y,1+max_y):
        for x in range(min_x,1+max_x):
            print( BLACK_char if (x,y) in points else WHITE_char, end="")
        print()


def process_data(data:str) -> tuple[list[Point],list[dict[str,int|str]]]:
    """transform the raw data into a procesable form"""
    _puntos, _folds = ir.isplit(data.splitlines(),"")
    puntos = [Point(*literal_eval(line)) for line in _puntos]
    folds = []
    for line in _folds:
        *_,fold = line.split()
        axis,val = fold.split("=")
        folds.append( {"axis":axis, "value":int(val)} )
    return puntos,folds
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




