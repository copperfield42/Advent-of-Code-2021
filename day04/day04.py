#https://adventofcode.com/2021/day/4
#from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
import numpy


test_input="""
7,4,9,5,11,17,23,2,0,14,21,24,10,16,13,6,15,25,12,22,18,20,8,19,3,26,1

22 13 17 11  0
 8  2 23  4 24
21  9 14 16  7
 6 10  3 18  5
 1 12 20 15 19

 3 15  0  2 22
 9 18 13 17  5
19  8  7 25 23
20 11 10 24  4
14 21 16 12  6

14 21 17 24  4
10 16 15  9 19
18  8 23 26 20
22 11 13  6  5
 2  0 12  3  7
"""

def process_data(data:str) -> tuple[list[int],list[numpy.ndarray[int]]]:
    """transform the raw data into a procesable form"""
    (header,),*matrices = ir.isplit(data.splitlines())
    header = list(map(int,header.split(",")))
    matrix = [numpy.array([list(map(int,f.split())) for f in m],dtype=int) for m in matrices]
    return header, matrix
        
def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

class BingoWinner(Exception):
    pass

class Bingo:

    def __init__(self, *board:numpy.ndarray[int]):
        self.boards = {i:b for i,b in enumerate(board)}
        
    def play(self, numbers:list[int]) -> Iterator[list[tuple[int,int]]]:
        state = {i:(b,b==-1) for i,b in self.boards.items()}
        or_ = numpy.logical_or
        for n in numbers:
            new_state = {i:(b,or_(s,b==n)) for i,(b,s) in state.items()}
            if (win:=self.check_for_winner(new_state, n)):
                yield win
                for w,_ in win:
                    del new_state[w]
            if not new_state:
                return
            state = new_state

    def check_for_winner(self, state:dict[int,tuple[numpy.ndarray[int],numpy.ndarray[bool]]], last_play:int) -> list[tuple[int,int]]:
        return [ (i,self.score(b,w,last_play)) for i,(b,w) in state.items() if (w.all(axis=0) | w.all(axis=1)).any()]

    def score(self, board, state, last_play):
        return last_play*( board[ state==False ].sum() )
        

        





def part1(data:str) -> int:
    """part 1 of the puzzle """
    nums, boards = process_data(data)
    Bin = Bingo(*boards)
    result = next(Bin.play(nums))
    return result[0][-1]



def part2(data:str) -> int:
    """part 2 of the puzzle """
    nums, boards = process_data(data)
    Bin = Bingo(*boards)
    result = ir.last(Bin.play(nums))
    return result[0][-1]
    
 
    
   
def test1() -> bool:
    return 4512 == part1(test_input)

def test2() -> bool:
    return 1924 == part2(test_input) 




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














