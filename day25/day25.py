# https://adventofcode.com/2021/day/25
from __future__ import annotations

from typing import Iterator
import itertools_recipes as ir
import numpy as np
from aoc_recipes import WHITE_char, get_raw_data
from dataclasses import dataclass, astuple, field

test_input = """
v...>>.vv>
.vv>>.vv..
>>.>v>...v
>>v>>.>.v.
v>v.vv.v..
>.>>..v...
.vv..>.>v.
v.v..>>v.v
....v..v.>
"""

test_input_2 = """
...>...
.......
......>
v.....>
......>
.......
..vvv..
"""


@dataclass
class SeaCucumbers(Iterator):
    data: np.ndarray[int, int]
    empty: str = WHITE_char
    east: str = ">"
    south: str = "v"
    _done: bool = field(init=False, default=False)

    def show(self):
        data, empty, east, south = astuple(self)[:4]
        X, Y = data.shape
        for y in range(Y):
            for x in range(X):
                match data[x, y]:
                    case 0:
                        c = empty
                    case 1:
                        c = east
                    case 2:
                        c = south
                    case error:
                        raise ValueError(f"unexpected cucumber value {error!r}")
                print(c, end="")
            print()

    def __next__(self):
        if self._done:
            raise StopIteration
        done = 0
        data = self.data
        for kind, axis in ((1, 0), (2, 1)):
            empty = data == 0
            pos_kind = data == kind
            next_pos = np.roll(pos_kind, shift=1, axis=axis)
            to_move = next_pos & empty
            if to_move.any():
                prev_pos = np.roll(to_move, shift=-1, axis=axis)
                data[prev_pos] = 0
                data[to_move] = kind
            else:
                done += 1
        if done >= 2:
            self._done = True
        return self


def process_data(data: str) -> SeaCucumbers:
    """transform the raw data into a processable form"""
    lines = list(ir.interesting_lines(data))
    cucumbers = np.zeros((len(lines[0]), len(lines)), dtype=np.int8)
    for y, line in enumerate(lines):
        for x, c in enumerate(line):
            match c:
                case ".":
                    n = 0
                case ">":
                    n = 1
                case "v":
                    n = 2
                case error:
                    raise ValueError(f"unexpected character {error!r}")
            cucumbers[x, y] = n
    return SeaCucumbers(cucumbers)


def test_run(data: str, steps: int = 4):
    cucu = process_data(data)
    print("Initial state:")
    cucu.show()
    print()
    for i, c in enumerate(ir.islice(cucu, steps), 1):
        print("After", i, "steps:")
        c.show()
        print()


def main(data: str) -> int:
    """part 1 of the puzzle """
    cucu = process_data(data)
    return sum(1 for _ in cucu)


def test() -> bool:
    return main(test_input) == 58


if __name__ == "__main__":
    assert test(), "fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data))  #
