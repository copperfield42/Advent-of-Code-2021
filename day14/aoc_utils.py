#https://adventofcode.com/2021/day/14
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from itertools import pairwise




test_input="""
NNCB

CH -> B
HH -> N
CB -> H
NH -> C
HB -> C
HC -> B
HN -> C
NN -> C
BH -> H
NC -> B
NB -> B
BN -> B
BB -> N
BC -> B
CC -> N
CN -> C
"""

def findall(text:str, patron:str) -> Iterator[int]:
    ini = 0
    while (i:=text.find(patron,ini)) != -1:
        yield i
        ini = i+1


def polymerization(polymer:str, pair_insertion:Iterable[tuple[str,str]]) -> str:
    subs = {i:insert for patron, insert in pair_insertion for i in findall(polymer, patron) }
    return "".join( c for i,o in enumerate(polymer) for c in (o,subs.get(i,"")))

def ipolymerization(text:Iterable[str], pair_insertion:dict[tuple[str,str],str]) -> Iterator[str]:
    pair = None
    for pair in pairwise(text):
        yield pair[0]
        if (extra:=pair_insertion.get(pair)):
            yield extra
    if pair:
        yield pair[1]


def process_data(data:str) -> tuple[str,list[tuple[str,str]]]:
    """transform the raw data into a procesable form"""
    it = ir.interesting_lines(data)
    template = next(it)
    rules = [tuple(x.split(" -> ")) for x in it]
    return template,rules
    
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




