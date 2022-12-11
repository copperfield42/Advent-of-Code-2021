#https://adventofcode.com/2021/day/3
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
from math import prod
from collections import defaultdict

test_input="""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
"""

def process_data(data:str) -> Iterator[tuple[int,int]]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data.splitlines()):
        yield int(line,2),len(line)
    
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def most_common_bit(data:list[tuple[int,int]]) -> dict[int,bool]:
    """said if a given bit is the most common in the data or not"""
    result = defaultdict(int)
    total = 0
    for total,(val, size) in enumerate(data,1):
        for shift in range(size):
            mask = 1<<shift
            result[mask] += bool(val & mask)
    return {mask:(val >= total/2) for mask,val in result.items()}

def part1(data:str) -> int:
    """part 1 of the puzzle """
    result = most_common_bit(process_data(data))
    gamma = 0
    for mask,val in result.items():
        gamma |= mask*val
    epsilon = ((max(result)<<1)-1)^gamma
    return gamma*epsilon


    
def bit_criteria_reduce(data:list[int], size:int, criteria:bool) -> int:
    while len(data)>1 and size>=0:
        common = most_common_bit( (x,size) for x in data )
        mask = max(common)
        data = [x for x in data if bool(x&mask)==(common[mask]==criteria) ]
        size -= 1
    assert len(data)==1,"no se redujo a un solo elemento"
    return data[0]  

def part2(data:str) -> int:
    """part 2 of the puzzle """
    bit_data, it2 = ir.unzip(process_data(data))
    size = max(it2)
    oxy = bit_criteria_reduce(bit_data, size, True)
    co2 = bit_criteria_reduce(bit_data, size, False)
    return oxy * co2
    
 
    
   
def test1() -> bool:
    return 198 == part1(test_input)

def test2() -> bool:
    return 230 == part2(test_input) 




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














