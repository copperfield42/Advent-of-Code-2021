#https://adventofcode.com/2021/day/16
from __future__ import annotations

from aoc_utils import get_raw_data, process_data
from aoc_utils import packet_decoder, Packet
from math import prod
import operator

test_input_dict = {
    "C200B40A82": 3,
    "880086C3E88112": 7,
    "CE00C43D881120": 9,
    "D8005AC2A8F0": 1, 
    "F600BC2D8F": 0,
    "9C005AC2F8F0": 0,
    "9C0141080250320F1802104A08": 1,
    "04005AC33890": 54,
    }


FUNCTIONS = { 
    0:sum,
    1:prod,
    2:min,
    3:max,
    5:lambda x:operator.gt(*x),
    6:lambda x:operator.lt(*x),
    7:lambda x:operator.eq(*x),
    }


def eval_packet(pack:Packet|int) -> int:
    if not isinstance(pack,Packet):
        return pack
    if pack.type_id == 4:
        return pack.value[0]
    return FUNCTIONS[pack.type_id](map(eval_packet,pack.value))
    



def main(data:str) -> int:
    """part 2 of the puzzle """
    return eval_packet(packet_decoder(process_data(data)))


def test() -> bool:
    return all( main(v) == r or print(f"fail {v!r} -> {r}") for v,r in test_input_dict.items() )



if __name__ == "__main__":
    assert test(),"fail test part 2"
    print("pass test part 2\n")
    data = get_raw_data()
    print("solution part2:", main(data)) # 184487454837
    













