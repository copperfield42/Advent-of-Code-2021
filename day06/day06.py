#https://adventofcode.com/2021/day/6
#from __future__ import annotations

from typing import Iterable, Iterator
#import itertools_recipes as ir
from collections import Counter





test_input="""
3,4,3,1,2
"""

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def process_data(data:str) -> Iterator[int]:
    """transform the raw data into a procesable form"""
    return map(int, data.split(","))
        

def lanternfish(initial:Iterable[int], days:int) -> int :
    """
    return the number of lanternfish after that many days
    given the initial condition
    """
    fishs = Counter(initial)
    for _ in range(days):
        new_f = Counter()
        for k,v in fishs.items():
            if k:
                new_f[k-1] += v
            else:
                new_f[6] += v
                new_f[8] += v
        fishs = new_f
    return fishs.total() 

    

def part1(data:str) -> int:
    """part 1 of the puzzle """
    return lanternfish(process_data(data),80)

    


def part2(data:str) -> int:
    """part 2 of the puzzle """
    return lanternfish(process_data(data),256)
    
 
    
   
def test1() -> bool:
    return part1(test_input) == 5934

def test2() -> bool:
    return part2(test_input) == 26984457539




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














