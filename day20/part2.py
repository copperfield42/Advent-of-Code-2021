#https://adventofcode.com/2021/day/20
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import enhance_img




def main(data:str) -> int:
    """part 2 of the puzzle """
    mask, img = process_data(data)
    for n in range(50):
        img = enhance_img(img, mask, fillvalue= (mask&1) if n%2 else 0)
    return img.sum()


def test() -> bool:
    return main(test_input) == 3351



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













