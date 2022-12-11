#https://adventofcode.com/2021/day/7
#from __future__ import annotations

from typing import Iterable, Iterator, Callable
#import itertools_recipes as ir
from collections import Counter





test_input="""
16,1,2,0,4,2,7,1,2,14
"""

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def process_data(data:str) -> Iterator[int]:
    """transform the raw data into a procesable form"""
    return map(int, data.split(","))
        
def calculate_fuel(data:dict[int,int], pos:int) -> int:
    return sum(abs(pos-k)*v for k,v in data.items() )
        
def calculate(data:dict[int,int], fuel_fun:Callable[[dict[int,int]],int]):
    max_pos = max(data.keys())
    return min( fuel_fun(data,p) for p in range(max_pos+1) )
    

def part1(data:str) -> int:
    """part 1 of the puzzle """
    return calculate(Counter(process_data(data)), calculate_fuel)



def triangular_number(n:int) -> int:
    return n*(n+1)//2

def calculate_fuel_2(data:dict[int,int], pos:int) -> int:
    return sum(triangular_number(abs(pos-k))*v for k,v in data.items() )
    


def part2(data:str) -> int:
    """part 2 of the puzzle """
    return calculate(Counter(process_data(data)), calculate_fuel_2)
    
 
    
   
def test1() -> bool:
    return part1(test_input) == 37

def test2() -> bool:
    return part2(test_input) == 168




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














