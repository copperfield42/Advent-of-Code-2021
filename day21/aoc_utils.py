# https://adventofcode.com/2021/day/21
from __future__ import annotations

from dataclasses import dataclass, field
from typing import Iterator, Iterable, Protocol
import itertools_recipes as ir
import re


class Dice(Iterator, Protocol):
    rolls: int

    def roll(self, times: int) -> int:
        ...


@dataclass
class DeterministicDie:
    sides: int = 100
    rolls: int = field(init=False, default=0)
    value: int = field(init=False, default=0)

    def __iter__(self):
        return self

    def __next__(self):
        val = (self.value + 1) % self.sides
        if not val:
            val = self.sides
        self.rolls += 1
        self.value = val
        return val

    def roll(self, times: int = 3):
        return ir.take(times, self, sum)

@dataclass
class DiracDice:
    players: dict[int, dict[str, int]] = field(init=False, default_factory=dict)
    dice: Dice = field(init=False, default_factory=DeterministicDie)

    def __init__(self, initial_pos: dict[int, int], dice: Dice | None = None):
        self.players = {}
        for p, pos in initial_pos.items():
            self.players[p] = {"pos":pos, "score":0}
        self.dice = dice or DeterministicDie()

    def play(self):
        dice = self.dice
        for i, p in enumerate(ir.cycle(sorted(self.players))):
            roll = dice.roll(3)
            new_pos = ((self.players[p]["pos"] + roll) % 10) or 10
            self.players[p]["pos"] = new_pos
            self.players[p]["score"] += new_pos
            if self.players[p]["score"] >= 1000:
                return dice.rolls, self.players
            #if i<11:
            #    print(f"{p=} {self.players[p]=}")


test_input="""
Player 1 starting position: 4
Player 2 starting position: 8
"""



def process_data(data:str) -> dict[int,int]:
    """transform the raw data into a procesable form"""
    result = {}
    for line in ir.interesting_lines(data):
        a,b = map(int,re.findall("(\d+)",line))
        result[a]=b
    return result
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




