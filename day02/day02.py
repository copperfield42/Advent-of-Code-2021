#https://adventofcode.com/2021/day/2
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
from math import prod
from collections import defaultdict

test_input="""
forward 5
down 5
forward 8
up 3
down 8
forward 2
"""

def process_data(data:str) -> Iterator[tuple[bool,int]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data.splitlines()):
        comm, num = line.split()
        num = int(num)
        if comm == "forward":
            yield True,num
        else:
            yield False,num*(1 if comm=="down" else (-1))

    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



def part1(data:str) -> int:
    """part 1 of the puzzle """
    result = defaultdict(int)
    for k,v in process_data(data):
        result[k]+=v
    return prod(result.values())
    
    

def part2(data:str) -> int:
    """part 2 of the puzzle """
    result = defaultdict(int)
    for isforward,v in process_data(data):
        if isforward:
            result["hpos"] += v
            result["death"]+= v*result["aim"]
        else:
            result["aim"]+=v
    del result["aim"]
    return prod(result.values()) 
    
 
    
   
def test1() -> bool:
    return 150 == part1(test_input)

def test2() -> bool:
    return 900 == part2(test_input) 




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














