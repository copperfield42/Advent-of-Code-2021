#https://adventofcode.com/2021/day/17
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from aoc_recipes import Point, WHITE_char, BLACK_char
from functools_recipes import dual_reduce, cached_property
from dataclasses import dataclass, astuple, field
from math import sqrt, floor
import re


test_input="""
target area: x=20..30, y=-10..-5
"""

@dataclass(eq=True, frozen=True)
class Target:
    min_x:int
    max_x:int
    min_y:int
    max_y:int
    
    def __contains__(self, otro:Point|complex) -> bool:
        if not isinstance(otro, (Point,tuple,complex)):
            return False
        if isinstance(otro, complex):
            x = otro.real
            y = otro.imag
        else:
            x,y = otro
        min_x,max_x,min_y,max_y = astuple(self) 
        return min_x <= x <= max_x and min_y <= y <= max_y 
    
    @cached_property
    def center(self) -> Point:
        min_x,max_x,min_y,max_y = astuple(self) 
        X = min_x+max_x
        Y = min_y+max_y
        c = Point(X//2,Y//2)
        if c in self:
            return c
        else:
            return Point(X/2,Y/2)
            
    @cached_property
    def corners(self):
        min_x,max_x,min_y,max_y = astuple(self) 
        return Point(min_x,max_y), Point(max_x,max_y), Point(min_x,min_y), Point(max_x,min_y)
            
    def pass_target_right(self, point:Point) -> Point:
        x,y = point
        min_x,max_x,min_y,max_y = astuple(self) 
        return x>max_x or y<min_y
    

@dataclass
class Probe:
    velocity:Point
    target:Target
    pos:Point = Point(0,0)
    done:bool = field(init=False, default=False)
    hit:bool = field(init=False, default=False)

    def __iter__(self):
        return self

    def __next__(self):
        pos = self.pos
        vel = self.velocity
        target = self.target
        if self.done:
            raise StopIteration
        if pos in target or target.pass_target_right(pos):
            self.done = True
            self.hit = pos in target
            return pos
        new_pos = pos + vel
        drag = 0
        if vel.x>0:
            drag = -1
        elif vel.x<0:
            drag = +1
        new_vel = vel + Point(drag,-1)
        self.pos = new_pos
        self.velocity = new_vel
        return pos


def sum_of_n(n:int) -> int:
    "n-triangular number"
    if n<0:
        return -sum_of_n(-n)
    return n*(n+1)//2


def calculate_min_x(dist:int) -> int:
    """calculate the minimun x-component of velocity 
       needed to reach dist"""
    test = floor(sqrt( dist*8+1 )/2)
    #the approximation to the triangular number that 
    #aproximate target.min_x because the maximun distance 
    #that the probe can reach is the triangular number 
    #assosiate with x component of the velocity
    assert sum_of_n(test)>=dist
    while sum_of_n(test-1)>=dist:
        test -= 1
    return test


def show(path:set[Point], target:Target, start:Point=Point(0,0)):
    points = {*path, start, *target.corners}
    min_x, max_x = dual_reduce(p.x for p in points)
    min_y, max_y = dual_reduce(p.y for p in points)
    for y in reversed(range(min_y,max_y+1)):
        for x in range(min_x,max_x+1):
            p = Point(x,y)
            c = WHITE_char
            if p == start:
                c = "S"
            else:
                if p in target:
                    c = BLACK_char
                if p in path:
                    c = "#"
            print(c,end="")
        print()



def process_data(data:str) -> Target:
    """transform the raw data into a procesable form"""
    return Target( *map(int,re.findall("(-?\d+)",data)) )
    
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




