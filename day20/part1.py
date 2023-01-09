#https://adventofcode.com/2021/day/20
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import enhance_img


def main(data:str) -> int:
    """part 1 of the puzzle """
    mask, img = process_data(data)
    img2 = enhance_img(img, mask)
    img3 = enhance_img(img2, mask, fillvalue=mask&1)
    return img3.sum()


def test() -> bool:
    return main(test_input) == 35



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












