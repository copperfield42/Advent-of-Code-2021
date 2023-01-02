#https://adventofcode.com/2021/day/12
from __future__ import annotations

from typing import Iterator, Iterable
import itertools_recipes as ir
from collections import defaultdict
from dataclasses import dataclass, field
import aoc_recipes



test_input="""
start-A
start-b
A-c
A-b
b-d
A-end
b-end
"""

test_input_list = [
    test_input,
    """
    dc-end
    HN-start
    start-kj
    dc-start
    dc-HN
    LN-dc
    HN-end
    kj-sa
    kj-HN
    kj-dc
    """,
    """
    fs-end
    he-DX
    fs-he
    start-DX
    pj-DX
    end-zg
    zg-sl
    zg-pj
    pj-he
    RW-he
    fs-DX
    pj-RW
    zg-RW
    start-pj
    he-WI
    zg-he
    pj-fs
    start-RW
    """
]

@dataclass
class Grafo:
    nodes:frozenset[str]
    edges:dict[str,frozenset[str,...]]
    big:tuple[str]   = field(init=False,default=None)
    small:tuple[str] = field(init=False, default=None)

    def __post_init__(self):
        ntype = defaultdict(list)
        for n in self.nodes:
            ntype[n.isupper()].append(n)
        self.big = tuple(ntype[True])
        self.small = aoc_recipes.make_mirror_dict(enumerate(ntype[False],1))


    def _all_paths_count(self, end:str, visitados:int, path:str) -> Iterator[int]:
        """count of all paths pasing by the small nodes at most once"""
        if path == end:
            yield 1
            return
        for vecino in self.edges[path]:
            if iv := self.small.get(vecino):
                i = 1 << iv
                if i&visitados:
                    continue
                yield from self._all_paths_count(end, visitados|i, vecino )
            else:
                yield from self._all_paths_count(end, visitados, vecino )


    def all_paths_count(self, start:str="start", end:str="end") -> int:
        """count of all paths pasing by the small nodes at most once"""
        path = start
        visitados = (1<<self.small[start]) if start in self.small else 0
        return sum(self._all_paths_count(end, visitados, path))


    def _all_paths_count2(self, end:str, visitados:int, path:str, do_twice:str, visited:int=0) -> Iterator[int]:
        """count of all paths pasing by the small nodes at most once and for specified one exactly twice"""
        if path == end :
            if visited == 2:
                yield 1
            return
        for vecino in self.edges[path]:
            if iv := self.small.get(vecino):
                i = 1 << iv
                if i&visitados:
                    continue
                else:
                    if vecino == do_twice:
                        new_visited = visited + 1
                        new_visitados = (i|visitados) if new_visited > 1 else visitados
                        yield from self._all_paths_count2(end, new_visitados, vecino, do_twice, new_visited )
                    else:
                        yield from self._all_paths_count2(end, visitados|i, vecino, do_twice, visited )
            else:
                yield from self._all_paths_count2(end, visitados, vecino, do_twice, visited )

    def all_paths_count2(self, start="start", end="end") -> int:
        """count of all paths pasing by the small nodes at most once
           plus all paths passing for a particular small node exactly twice """
        path = start
        visitados = (1<<self.small[start]) if start in self.small else 0
        result = sum(self._all_paths_count(end, visitados, path))
        for n in self.nodes:
            if n in self.small and n not in {start,end}:
               result += sum(self._all_paths_count2(end, visitados, path, n, 0))
        return result


def process_data(data:str) -> Grafo:
    """transform the raw data into a procesable form"""
    nodes = set()
    edges = defaultdict(set)
    for a,b in ( line.split("-") for line in ir.interesting_lines(data) ):
        nodes.add(a)
        nodes.add(b)
        edges[a].add(b)
        edges[b].add(a)
    return Grafo(frozenset(nodes), {k:frozenset(v) for k,v in edges.items()})



def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()




