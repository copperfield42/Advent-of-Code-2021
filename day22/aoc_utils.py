# https://adventofcode.com/2021/day/22
from __future__ import annotations

import re
from dataclasses import dataclass, astuple
from itertools import product, pairwise
from math import prod
from typing import Iterator, Iterable, NamedTuple
import itertools_recipes as ir
from aoc_recipes import Point3

test_input="""
on x=-20..26,y=-36..17,z=-47..7
on x=-20..33,y=-21..23,z=-26..28
on x=-22..28,y=-29..23,z=-38..16
on x=-46..7,y=-6..46,z=-50..-1
on x=-49..1,y=-3..46,z=-24..28
on x=2..47,y=-22..22,z=-23..27
on x=-27..23,y=-28..26,z=-21..29
on x=-39..5,y=-6..47,z=-3..44
on x=-30..21,y=-8..43,z=-13..34
on x=-22..26,y=-27..20,z=-29..19
off x=-48..-32,y=26..41,z=-47..-37
on x=-12..35,y=6..50,z=-50..-2
off x=-48..-32,y=-32..-16,z=-15..-5
on x=-18..26,y=-33..15,z=-7..46
off x=-40..-22,y=-38..-28,z=23..41
on x=-16..35,y=-41..10,z=-47..6
off x=-32..-23,y=11..30,z=-14..3
on x=-49..-5,y=-3..45,z=-29..18
off x=18..30,y=-20..-8,z=-3..13
on x=-41..9,y=-7..43,z=-33..15
on x=-54112..-39298,y=-85059..-49293,z=-27449..7877
on x=967..23432,y=45373..81175,z=27513..53682
"""


test_input_small = """
on x=10..12,y=10..12,z=10..12
on x=11..13,y=11..13,z=11..13
off x=9..11,y=9..11,z=9..11
on x=10..10,y=10..10,z=10..10
"""

def overlap(a:tuple[int,int], b:tuple[int,int]) -> bool:
    x1, y1 = a
    x2, y2 = b
    return x1 < y2 and x2 < y1 #y1 > x2
    #return ((x1 <= x2 < y1) or (x1 <= y2 < y1)) or \
    #       ((x2 <= x1 < y2) or (x2 <= y1 < y2))


class Cuboid(NamedTuple):
    x_range: tuple[int, int]
    y_range: tuple[int, int]
    z_range: tuple[int, int]

    @property
    def parts(self):
        return self.x_range, self.y_range, self.z_range

    def __iter__(self) -> Iterator[Point3]:
        return ir.starmap(Point3, ir.product(range(*self.x_range), range(*self.y_range), range(*self.z_range)))

    def __contains__(self, item: Point3 | Cuboid) -> bool:
        #print("__contains__", self, item, sep="\n")
        if not isinstance(item, (tuple, Point3, type(self))):
            return False
        if isinstance(item, type(self)):
            return all(ini1 <= ini2 and fin2 <= fin1 for (ini1, fin1), (ini2, fin2) in zip(self.parts, item.parts))
        if isinstance(item, (tuple, Point3)):
            try:
                return all(ini <= c < fin for c, (ini, fin) in zip(item, self.parts, strict=True))
            except ValueError:
                return False
        return False


    def __len__(self):
        return prod(len(range(ini, fin)) for ini, fin in self.parts)

    def sub_cuboid(self, item:Cuboid) -> Cuboid:
        if not isinstance(item, type(self)):
            raise ValueError("item is not a Cuboid")
        args = []
        for this, otro in zip(self.parts, item.parts):
            ini1, fin1 = this
            ini2, fin2 = otro
            ini:int = ini1 if ini2 <= ini1 else ini2
            fin:int = fin1 if fin1 <= fin2 else fin2
            args.append((ini, fin))
        return type(self)(*args)

    def __and__(self, other: Cuboid) -> bool:
        """said if the cuboids intersect"""
        if not isinstance(other, type(self)):
            return NotImplemented
        return all(map(overlap, self.parts, other.parts))

    intersects = __and__

    def subtract(self, other: Cuboid) -> Iterator[Cuboid]:
        #print("subtract", self, other, sep="\n")
        if not isinstance(other, type(self)):
            raise ValueError("not a cuboid")
        if not self & other:
            yield self
        if self in other:
            return
        xs = sorted(self.x_range + other.x_range)
        ys = sorted(self.y_range + other.y_range)
        zs = sorted(self.z_range + other.z_range)
        for x, y, z in product(pairwise(xs), pairwise(ys), pairwise(zs)):
            c = type(self)(x, y, z)
            if not c:
                continue
            if c in self and not c & other:
                yield c

    def __sub__(self, other: Cuboid) -> tuple[Cuboid]:
        try:
            return tuple(self.subtract(other))
        except ValueError:
            return NotImplemented




def process_data(data:str) -> list[tuple[Cuboid,bool]]:
    """transform the raw data into a procesable form"""
    result = []
    for line in ir.interesting_lines(data):
        args = []
        for coord in re.findall(r"([xyz]\=\-?\d+\.\.\-?\d+)", line):
            a,b = re.findall(r"-?\d+", coord)
            args.append((int(a), int(b)+1))
        result.append( (Cuboid(*args), line.startswith("on")) )
    return result
    
    

def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




