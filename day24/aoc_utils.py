# https://adventofcode.com/2021/day/24
from __future__ import annotations

import operator
from dataclasses import dataclass, asdict, astuple
from fractions import Fraction
from typing import Iterator, Iterable, Callable
import itertools_recipes as ir




test_input="""
inp w
add z w
mod z 2
div w 2
add y w
mod y 2
div w 2
add x w
mod x 2
div w 2
mod w 2
"""


@dataclass
class ALU:
    w: int = 0
    x: int = 0
    y: int = 0
    z: int = 0

    def operation(self, register: str, value: str | int, function: Callable[[int, int], int]):
        r = getattr(self, register)
        if isinstance(value, str):
            value = getattr(self, value)
        setattr(self, register, function(r, value))

    def add(self, register: str, value: str | int):
        self.operation(register, value, operator.add)

    def mul(self, register: str, value: str | int):
        self.operation(register, value, operator.mul)

    def div(self, register: str, value: str | int):
        #def division(x, y):
        #    if y == 1:
        #        return x
        #    return x // y
        self.operation(register, value, operator.floordiv)

    def mod(self, register: str, value: str | int):
        self.operation(register, value, operator.mod)

    def eql(self, register: str, value: str | int):
        #def igual(x, y):
        #    result = x==y
        #    if isinstance(result, bool):
        #        return int(result)
        #    return result
        self.operation(register, value, operator.eq)

    def inp(self, register, value: int = 0):
        setattr(self, register, value)
    
    def __str__(self):
        return "\n".join([type(self).__name__,*(f"{k}={v}" for k,v in asdict(self).items())])


@dataclass
class MONAD:
    instructions: list[tuple[str, str] | tuple[str, str, str | int]]

    def run(self, value: Iterable[int], show: bool = False) -> ALU:  # , corrections: dict[int, tuple[str, int]] = None) -> ALU:
        value = iter(value)
        alu = ALU()
        for i, (ins, *arg) in enumerate(self.instructions):
            if ins == "inp":
                alu.inp(arg[0], next(value))
            else:
                fun = getattr(alu, ins)
                fun(*arg)
            # if corrections and i in corrections:
                # ind, val = corrections[i]
                # old = getattr(alu, ind)
                # setattr(alu, ind, val)
                # if show:
                    # print("apply correction")
                    # print(f"descartado {ind}={old!s}")
                    # print(f"reemplasado por:", val)
            if show:
                print(ins, arg, f"({i})")
                print(alu)
                #for ind in "wxyz":
                #    print(f"{ind}=", getattr(alu, ind))

                print("------")

        return alu

        pass



def process_data(data:str) -> MONAD:
    """transform the raw data into a procesable form"""
    def fun(text: str) -> tuple[str, str] | tuple[str, str, str | int]:
        ins, *data = text.split()
        if len(data) == 1:
            return ins, data[0]
        assert len(data) == 2
        y: str | int
        x, y = data
        if not y.isalpha():
            y = int(y)
        return ins, x, y
    return MONAD(list(map(fun, ir.interesting_lines(data))))
    

def get_raw_data(path: str = "./input.txt") -> str:
    with open(path) as file:
        return file.read()




