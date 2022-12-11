#https://adventofcode.com/2021/day/1
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir

test_input="""
199
200
208
210
200
207
240
269
260
263
"""

def process_data(data:str) -> Iterator[int]:
    """transform the raw data into a procesable form"""
    return map(int,data.split())
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()



def part1(data:str) -> int:
    """part 1 of the puzzle """
    return sum( c<n for c,n in ir.pairwise(process_data(data)))
    

def part2(data:str) -> int:
    """part 2 of the puzzle """
    return sum( c<n for  c,n in ir.pairwise( map(sum,ir.groupwise(process_data(data),3))))
     
    
 
    
   
def test1() -> bool:
    return 7 == part1(test_input)

def test2() -> bool:
    return 5 == part2(test_input) 




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














