#https://adventofcode.com/2021/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Grafo, test_input_list




def main(data:str) -> int:
    """part 1 of the puzzle """
    grafo = process_data(data)
    return grafo.all_paths_count()


def test() -> bool:
    return all( main(test_data) == result for test_data, result in zip(test_input_list,[10,19,226]) )

        



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 4573
    












