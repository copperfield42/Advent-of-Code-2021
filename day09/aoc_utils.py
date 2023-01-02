#https://adventofcode.com/2021/day/09
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
import numpy
from scipy.signal import convolve2d
from num_bases import num_dig




test_input="""
2199943210
3987894921
9856789892
8767896789
9899965678
"""


CON = numpy.array([ [    0, 11**1,      0],
                    [11**2,     1 , 11**4],
                    [    0, 11**3 ,     0],], dtype=int)



@numpy.vectorize
def is_low(num:int) -> bool:
    n,*res = num_dig(num,base=11)
    return all(n<x for x in res if x)


def find_low_point(data:numpy.ndarray[int,int]) -> numpy.ndarray[bool,bool]:
    con = convolve2d(data+1,CON,mode="same")
    return is_low(con)


def process_data(data:str) -> numpy.ndarray[int,int]:
    """transform the raw data into a procesable form"""
    return numpy.array([list(map(int,line)) for line in ir.interesting_lines(data)],dtype=int)
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()


#-------------------------------------------------------------------------------


