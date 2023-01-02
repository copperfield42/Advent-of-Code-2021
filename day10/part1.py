#https://adventofcode.com/2021/day/10
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import SCORE_CORRUCT, CorructedChunk, parse



def main(data:str,show=False) -> int:
    """part 1 of the puzzle """
    corruct = []
    for i,line in enumerate(process_data(data)):
        try:
            parse(line)
        except ValueError:
            pass
        except CorructedChunk as e:
            if show:print(f"line {i}: Expected {e.expected!r}, but found {e.got!r} instead.")
            corruct.append(e.got)
    return sum(SCORE_CORRUCT[c] for c in corruct)


def test() -> bool:
    return main(test_input,1) == 26397



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 
    












