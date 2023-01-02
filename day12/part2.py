#https://adventofcode.com/2021/day/12
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import Grafo, test_input_list




def main(data:str) -> int:
    """part 2 of the puzzle """
    grafo = process_data(data)
    return grafo.all_paths_count2()


def test() -> bool:
    return all( main(test_data) == result for test_data, result in zip(test_input_list,[36,103,3509]) )



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













