#https://adventofcode.com/2021/day/15
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy
from aoc_recipes import shortest_path_grafo, make_vecinos, is_valid, Point




test_input="""
1163751742
1381373672
2136511328
3694931569
7463417111
1319128137
1359912421
3125421639
1293138521
2311944581
"""





def calculate_risk(data:numpy.ndarray[int,int]) -> int:
    x,y = data.shape
    goal = Point(x-1,y-1)
    risk,_ = shortest_path_grafo(
        Point(0,0),
        goal,
        data,
        lambda point,m: make_vecinos(point,lambda p:is_valid(p,m.shape)),
        lambda a,p,acc,matrix: acc + matrix[p]
        )
    return risk


def process_data(data:str) -> numpy.ndarray[int,int]:
    """transform the raw data into a procesable form"""
    return numpy.array( [list(map(int,line)) for line in ir.interesting_lines(data)], dtype=int)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




