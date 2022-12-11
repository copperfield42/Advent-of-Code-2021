#https://adventofcode.com/2021/day/4
from __future__ import annotations

from typing import Iterator, NamedTuple
import itertools_recipes as ir
from math import copysign
from collections import Counter

class Point(NamedTuple):
    x: int
    y: int

    def __add__(self, otro:Point):
        x,y = self
        if isinstance(otro,type(self)):
            ox, oy = otro
        elif isinstance(otro, (int,float)):
            ox, oy = otro,otro
        else:
            return NotImplemented
        return type(self)(x+ox, y+oy)

    def __radd__(self, otro:Point):
        return self + otro

    def __neg__(self):
        x,y = self
        return type(self)(-x, -y)

    def __sub__(self, otro:Point):
        return self + (-otro)

    def normalize(self):
        x,y = self
        return type(self)(x and int(copysign(1,x)),y and int(copysign(1,y)))


class Line(NamedTuple):
    ini:Point
    end:Point

    def is_axis(self,) -> bool:
        "is horizontal or vertical line"
        p1,p2 = self
        return (p1.x == p2.x ) or (p1.y == p2.y)

    def points(self) -> Iterator[Point]:
        p1,p2 = self
        while p1!=p2:
            yield p1
            p1 = p1+(p2 -p1).normalize()
        yield p2



test_input="""
0,9 -> 5,9
8,0 -> 0,8
9,4 -> 3,4
2,2 -> 2,1
7,0 -> 7,4
6,4 -> 2,0
0,9 -> 2,9
3,4 -> 1,4
0,0 -> 8,8
5,5 -> 8,2
"""

def process_data(data:str) -> Iterator[Line]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield Line(*( Point(*map(int,p.split(","))) for p in line.split("->") ))

        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




def part1(data:str) -> int:
    """part 1 of the puzzle """
    count = Counter(ir.chain.from_iterable( line.points() for line in process_data(data) if line.is_axis()))

    return sum( x>1 for x in count.values())



def part2(data:str) -> int:
    """part 2 of the puzzle """
    count = Counter(ir.chain.from_iterable( line.points() for line in process_data(data) ))

    return sum( x>1 for x in count.values())
    
 
    
   
def test1() -> bool:
    return 5 == part1(test_input)

def test2() -> bool:
    return 12 == part2(test_input) 




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














