#https://adventofcode.com/2021/day/10
from __future__ import annotations

from aoc_utils import test_input, get_raw_data, process_data
from aoc_utils import parse, CorructedChunk, CHUNK_PAIRS, SCORE_INCOMPLE


def get_score(text:Iterable[str]) -> int:
    total = 0
    for c in text:
        total = total*5 + SCORE_INCOMPLE[c]
    return total
        


def main(data:str , show=False) -> int:
    """part 2 of the puzzle """
    score = []
    for i,line in enumerate(process_data(data)):
        try:
            result = parse(line)
            score.append( get_score(CHUNK_PAIRS[c] for c in result) )
            if show: print(i,line,"->","".join(CHUNK_PAIRS[c] for c in result))
        except (CorructedChunk, ValueError):
            pass
    score.sort()
    return score[len(score)//2]


def test() -> bool:
    return main(test_input,1) == 288957



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) #
    













