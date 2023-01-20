# https://adventofcode.com/2021/day/22
from __future__ import annotations

import operator
from dataclasses import dataclass, astuple
from functools import total_ordering
from itertools import product
from math import prod
from pprint import pprint
from typing import NamedTuple, Iterable
import random_functions

from aoc_utils import test_input, get_raw_data, process_data, Cuboid

test_input_2 = """
on x=-5..47,y=-31..22,z=-19..33
on x=-44..5,y=-27..21,z=-14..35
on x=-49..-1,y=-11..42,z=-10..38
on x=-20..34,y=-40..6,z=-44..1
off x=26..39,y=40..50,z=-2..11
on x=-41..5,y=-41..6,z=-36..8
off x=-43..-33,y=-45..-28,z=7..25
on x=-33..15,y=-32..19,z=-34..11
off x=35..47,y=-46..-34,z=-11..5
on x=-14..36,y=-6..44,z=-16..29
on x=-57795..-6158,y=29564..72030,z=20435..90618
on x=36731..105352,y=-21140..28532,z=16094..90401
on x=30999..107136,y=-53464..15513,z=8553..71215
on x=13528..83982,y=-99403..-27377,z=-24141..23996
on x=-72682..-12347,y=18159..111354,z=7391..80950
on x=-1060..80757,y=-65301..-20884,z=-103788..-16709
on x=-83015..-9461,y=-72160..-8347,z=-81239..-26856
on x=-52752..22273,y=-49450..9096,z=54442..119054
on x=-29982..40483,y=-108474..-28371,z=-24328..38471
on x=-4958..62750,y=40422..118853,z=-7672..65583
on x=55694..108686,y=-43367..46958,z=-26781..48729
on x=-98497..-18186,y=-63569..3412,z=1232..88485
on x=-726..56291,y=-62629..13224,z=18033..85226
on x=-110886..-34664,y=-81338..-8658,z=8914..63723
on x=-55829..24974,y=-16897..54165,z=-121762..-28058
on x=-65152..-11147,y=22489..91432,z=-58782..1780
on x=-120100..-32970,y=-46592..27473,z=-11695..61039
on x=-18631..37533,y=-124565..-50804,z=-35667..28308
on x=-57817..18248,y=49321..117703,z=5745..55881
on x=14781..98692,y=-1341..70827,z=15753..70151
on x=-34419..55919,y=-19626..40991,z=39015..114138
on x=-60785..11593,y=-56135..2999,z=-95368..-26915
on x=-32178..58085,y=17647..101866,z=-91405..-8878
on x=-53655..12091,y=50097..105568,z=-75335..-4862
on x=-111166..-40997,y=-71714..2688,z=5609..50954
on x=-16602..70118,y=-98693..-44401,z=5197..76897
on x=16383..101554,y=4615..83635,z=-44907..18747
off x=-95822..-15171,y=-19987..48940,z=10804..104439
on x=-89813..-14614,y=16069..88491,z=-3297..45228
on x=41075..99376,y=-20427..49978,z=-52012..13762
on x=-21330..50085,y=-17944..62733,z=-112280..-30197
on x=-16478..35915,y=36008..118594,z=-7885..47086
off x=-98156..-27851,y=-49952..43171,z=-99005..-8456
off x=2032..69770,y=-71013..4824,z=7471..94418
on x=43670..120875,y=-42068..12382,z=-24787..38892
off x=37514..111226,y=-45862..25743,z=-16714..54663
off x=25699..97951,y=-30668..59918,z=-15349..69697
off x=-44271..17935,y=-9516..60759,z=49131..112598
on x=-61695..-5813,y=40978..94975,z=8655..80240
off x=-101086..-9439,y=-7088..67543,z=33935..83858
off x=18020..114017,y=-48931..32606,z=21474..89843
off x=-77139..10506,y=-89994..-18797,z=-80..59318
off x=8476..79288,y=-75520..11602,z=-96624..-24783
on x=-47488..-1262,y=24338..100707,z=16292..72967
off x=-84341..13987,y=2429..92914,z=-90671..-1318
off x=-37810..49457,y=-71013..-7894,z=-105357..-13188
off x=-27365..46395,y=31009..98017,z=15428..76570
off x=-70369..-16548,y=22648..78696,z=-1892..86821
on x=-53470..21291,y=-120233..-33476,z=-44150..38147
off x=-93533..-4276,y=-16170..68771,z=-104985..-24507
"""

@total_ordering
@dataclass(eq=True)
class RangeSet:
    ini: int
    fin: int

    def __post_init__(self):
        ini, fin = astuple(self)
        if ini > fin:
            self.ini = 0
            self.fin = -1

    def __hash__(self):
        return hash(astuple(self))

    def __iter__(self) -> Iterable[int]:
        return iter(range(self.ini, self.fin+1))

    def __len__(self) -> ini:
        return len(range(self.ini, self.fin+1))

    def __lt__(self, other: RangeSet) -> bool:
        """self < other """
        if not isinstance(other, type(self)):
            return NotImplemented
        if (not self and other) or (not self and not other):
            return True
        if not other and self:
            return False
        x1, y1 = astuple(self)
        x2, y2 = astuple(other)
        return x2 <= x1 and y1 <= y2

    def __sub__(self, other:RangeSet) -> RangeSet | tuple[RangeSet, RangeSet]:
        """self - other"""
        if not isinstance(other, type(self)):
            return NotImplemented
        new = type(self)
        if not self or self < other:
            return new(0, -1)
        x1, y1 = astuple(self)
        x2, y2 = astuple(other)
        new = type(self)
        if y2 < x1 or y1 < x2:
            return new(x1, y1)
        if x2 <= x1 <= y2:
            return new(y2,y1)
        if x2 <= y1 <= y2:
            return new(x1,x2)
        if other < self:
            return new(x1, x2), new(y2, y1)

    def __add__(self, other:RangeSet) -> RangeSet | tuple[RangeSet, RangeSet]:
        if not isinstance(other, type(self)):
            return NotImplemented
        if not self:
            return other
        if not other:
            return self
        if self < other:
            return other
        if other < self:
            return self
        new:type[RangeSet] = type(self)
        x1, y1 = astuple(self)
        x2, y2 = astuple(other)
        if x2 <= x1 <= y2:
            return new(x2,max(y1,y2))
        if x2 <= y1 <= y2:
            return new(min(x1,x2), y2)
        if y1 < x2:
            return self, other
        else:
            return other, self


class UnionRange:

    def __init__(self):
        self.data:list[tuple[int, int]] = []

    def add(self, range_item:tuple[int, int]):
        pass
        #if any( es_contenid )


def compact_range(range_list: list[RangeSet]) -> list[RangeSet]:
    range_list = sorted(range_list, key=lambda x: x.ini)
    new = []
    a = range_list.pop(0)
    for b in range_list:
        c = a + b
        if isinstance(c, tuple):
            t, a = c
            new.append(t)
        else:
            a = c
    new.append(a)
    return [r for r in new if r]



def subtract_range(range_list:list[RangeSet], item:RangeSet) -> list[RangeSet]:
    range_list = compact_range(range_list)
    new = []
    for x in range_list:
        c = x - item
        if isinstance(c, tuple):
            new.extend(t for t in c if t)
        elif c:
            new.append(c)
    return new


def main_part1_v2(data:str, show:bool=False) -> int:
    """part 1 of the puzzle """
    on_cubes:dict[str, list[RangeSet]] = {"x": [], "y": [], "z": []}
    cubo50 = Cuboid((-50, 50 + 1), (-50, 50 + 1), (-50, 50 + 1))
    cubo:Cuboid
    for cubo, is_on in process_data(data).items():
        cubo = cubo.sub_cuboid(cubo50)
        for axis, pair in zip("xyz",astuple(cubo)):
            ran_a = RangeSet(*pair)
            if not ran_a:
                continue
            if is_on:
                on_cubes[axis] = compact_range(on_cubes[axis]+[ran_a])
            else:
                on_cubes[axis] = subtract_range(on_cubes[axis], ran_a)
    if show:
        pprint(on_cubes)
    return [ Cuboid(x,y,z) for x,y,z in product(map(astuple,on_cubes["x"]),map(astuple,on_cubes["y"]),map(astuple,on_cubes["z"]))]


def main_part1_set(data:str) -> int:
    """part 1 of the puzzle """
    on_cubes = set()
    cubo50 = Cuboid((-50, 50 + 1), (-50, 50 + 1), (-50, 50 + 1))
    work: Cuboid
    for work, val in progress_bar(process_data(data).items(), position=0):
        pwork = progress_bar(work.sub_cuboid(cubo50), position=1, leave=False)
        if val:
            on_cubes.update(pwork)
        else:
            on_cubes.difference_update(pwork)
    return on_cubes

def main(data:str, show:bool=False) -> int:
    """part 2 of the puzzle """
    on_cubes:dict[str, list[RangeSet]] = {"x": [], "y": [], "z": []}
    cubo:Cuboid
    for cubo, is_on in process_data(data).items():
        for axis, pair in zip("xyz",astuple(cubo)):
            ran_a = RangeSet(*pair)
            if is_on:
                on_cubes[axis] = compact_range(on_cubes[axis]+[ran_a])
            else:
                on_cubes[axis] = subtract_range(on_cubes[axis], ran_a)
    if show:
        pprint(on_cubes)
    return prod( sum(map(len,r)) for r in on_cubes.values())



def test() -> bool:
    return main(test_input_2) == 2758514936282235


def progress_bar(x,*a,**k):
    return x

A = main_part1_set(test_input)
B = main_part1_v2(test_input)
print(f"{len(A)=}")
pprint(B)
C = set()
C.update(*B)
print(f"{len(C)}")
if not A == C:
    print("no es lo mismo :(")
    print("A-C", len(A-C))
    print("C-A", len(C-A))
    print(f"A xs", random_functions.compact_range(p.x for p in A))
    print(f"A ys", random_functions.compact_range(p.y for p in A))
    print(f"A zs", random_functions.compact_range(p.z for p in A))
    print(f"C xs", random_functions.compact_range(p.x for p in C))
    print(f"C ys", random_functions.compact_range(p.y for p in C))
    print(f"C zs", random_functions.compact_range(p.z for p in C))
    assert 0
print("expected",590784)

if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













