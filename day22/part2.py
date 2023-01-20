# https://adventofcode.com/2021/day/22
from __future__ import annotations

from itertools import product, pairwise
from typing import NamedTuple

from aoc_utils import test_input_small, get_raw_data, process_data


class Cuboid3(NamedTuple):
    """ https://www.youtube.com/watch?v=dp0eCWc9gv8 """
    x_min: int
    x_max: int
    y_min: int
    y_max: int
    z_min: int
    z_max: int

    @property
    def size(self) -> int:
        return (
            (self.x_max - self.x_min) *
            (self.y_max - self.y_min) *
            (self.z_max - self.z_min)
        )

    @property
    def x_range(self) -> tuple[int, int]:
        return self.x_min, self.x_max

    @property
    def y_range(self) -> tuple[int, int]:
        return self.y_min, self.y_max

    @property
    def z_range(self) -> tuple[int, int]:
        return self.z_min, self.z_max

    def __and__(self, other: Cuboid3) -> bool:
        if not isinstance(other, type(self)):
            return NotImplemented
        return (
            self.x_min < other.x_max and
            other.x_min < self.x_max and
            self.y_min < other.y_max and
            other.y_min < self.y_max and
            self.z_min < other.z_max and
            other.z_min < self.z_max
        )

    def intersects(self, other: Cuboid3) -> bool:
        res = self & other
        if res is NotImplemented:
            raise ValueError("Not a Cuboid3")
        return res

    def __contains__(self, item: Cuboid3) -> bool:
        if not isinstance(item, type(self)):
            return False
        return (
            self.x_min <= item.x_min and
            item.x_max <= self.x_max and
            self.y_min <= item.y_min and
            item.y_max <= self.y_max and
            self.z_min <= item.z_min and
            item.z_max <= self.z_max
        )

    def __sub__(self, other: Cuboid3) -> list[Cuboid3]:
        if not isinstance(other, type(self)):
            return NotImplemented
        if not self & other:
            return [self]
        if self in other:
            return []
        xs = sorted((*self.x_range, *other.x_range))
        ys = sorted((*self.y_range, *other.y_range))
        zs = sorted((*self.z_range, *other.z_range))
        cubos = []
        for xp, yp, zp in product(pairwise(xs), pairwise(ys), pairwise(zs)):
            cubo = type(self)(*xp, *yp, *zp)
            if cubo in self and not cubo & other:
                cubos.append(cubo)
        return cubos




def main(data:str) -> int:
    """part 2 of the puzzle """
    cubos: list[Cuboid3] = []
    for oldc, add in process_data(data):
        cubo = Cuboid3(*oldc.x_range, *oldc.y_range, *oldc.z_range)
        cubos = [
            cubitos
            for kubo in cubos
            for cubitos in (kubo - cubo)
        ]
        if add:
            cubos.append(cubo)
    print(len(cubos))
    return sum(c.size for c in cubos)

    return


def test() -> bool:
    return main(test_input_small) == 39 and main(get_raw_data("test_input_medium.txt")) == 2758514936282235



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) # 1162571910364852
    













