#https://adventofcode.com/2021/day/16
from __future__ import annotations

from aoc_utils import get_raw_data, process_data
from aoc_utils import packet_decoder, Packet



test_input_dict = {
    "8A004A801A8002F478":16,
    "620080001611562C8802118E34":12,
    "C0015000016115A2E0802F182340":23,
    "A0016C880162017C3686B18A3D4780":31,
    }


def version_sum(packet:Packet) -> int:
    work = [packet]
    result = 0
    while work:
        p = work.pop()
        result += p.version
        for np in p.value:
            if isinstance(np,Packet):
                work.append(np)
    return result


def main(data:str) -> int:
    """part 1 of the puzzle """
    return version_sum(packet_decoder(process_data(data)))


def test() -> bool:
    return all( main(v) == r or print(f"fail {v!r} -> {r}") for v,r in test_input_dict.items() )



if __name__ == "__main__":
    assert test(),"fail test part 1"
    print("pass test part 1\n")
    data = get_raw_data()
    print("solution part1:", main(data)) # 886
    












