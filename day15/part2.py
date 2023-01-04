#https://adventofcode.com/2021/day/15
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import calculate_risk
from aoc_recipes import Point, is_valid


class ExpandMatrix:

    def __init__(self, data:numpy.ndarray[int,int]):
        self.data = data
        x,y = data.shape
        self.shape = (x*5, y*5)

    def __getitem__(self, coord:Point) -> int:
        dc,mc = divmod(coord, self.data.shape)
        val = (self.data[mc] + sum(dc) )%9
        if not val:
            val = 9
        return val

    def show(self):
        X,Y = self.shape
        for x in range(X):
            for y in range(Y):
                print(self[Point(x,y)],end="")
            print()


def main(data:str) -> int:
    """part 2 of the puzzle """
    data = ExpandMatrix(process_data(data))
    return calculate_risk(data)


def test() -> bool:
    return main(test_input) == 315



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #














