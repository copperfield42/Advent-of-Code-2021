#https://adventofcode.com/2021/day/16
from __future__ import annotations

from typing import NamedTuple, Protocol, runtime_checkable, Sized

@runtime_checkable
class BitReader(Sized, Protocol):
    def read(size:int|None) -> int:
        ...
    


def bites_size(n:int) -> int:
    d,m = divmod(n.bit_length(),4)
    return (d+bool(m))*4


class Packet(NamedTuple):
    version:int
    type_id:int
    value:list[int|Packet]


class BitChunker:
    """class to help optain chunk of bits from the right of the given number"""

    def __init__(self, number:int, size:int=None):
        self.num = number
        if size is None:
            size = bites_size(number)
        if not number:
            sise=0
        self.size = size
        self._size = size

    def __repr__(self):
        return f"{type(self).__name__}(0x{self.num:0X}, {self.size})"

    def __iter__(self):
        mask = 1<<(self._size-1)
        num = self.num
        while mask:
            yield not not mask&num
            mask >>= 1

    def __len__(self):
        return self.size

    def read(self, size:int=None) -> int:
        cur_size = self.size
        if not cur_size:
            raise ValueError("empty pack")
        if size is None or size>cur_size:
            size = cur_size
        if size<0:
            raise ValueError("negative size")
        mask = (1<<cur_size)-1
        result = (self.num & mask)>>(cur_size-size)
        self.size -= size
        return result

    def reset(self):
        self.size = self._size


def show(pack:Packet, iden:int=0):
    if isinstance(pack,Packet):
        print(" "*iden, f"version={pack.version} type_id={pack.type_id}{{", sep="")
        for v in pack.value:
            show(v,iden+2)
        print(" "*iden, "}", sep="")
    else:
        print(" "*iden, pack, sep="")         


def literal_value_pack(pack:BitReader, version:int, type_id:int) -> Packet:
    result = 0
    while True:
        chunck = pack.read(5)
        result |= chunck & 0b1111
        if chunck & 0b10000:
            result <<= 4
        else:
            break
    return Packet( version, type_id, [result] )


def operator_pack(pack:BitReader, V:int, T:int) -> Packet:
    I = pack.read(1)
    L = pack.read(11 if I else 15)
    if I:
        result = [ packet_decoder(pack) for _ in range(L) ]
    else:
        result = []
        read = len(pack)
        while (read-len(pack))<L:
            sub = packet_decoder(pack) 
            result.append(sub)
    return Packet(V,T,result)


def packet_decoder(pack:BitReader) -> Packet:
    version = pack.read(3)
    type_id = pack.read(3)
    if type_id==4:
        return literal_value_pack(pack, version, type_id)
    else:
        return operator_pack(pack, version, type_id)



def process_data(data:str) -> BitReader:
    """transform the raw data into a procesable form"""
    data = data.strip()
    ndata = int(data,16)
    return BitChunker(ndata, len(data)*4)



def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




