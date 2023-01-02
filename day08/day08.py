#https://adventofcode.com/2021/day/8
#from __future__ import annotations

from typing import Iterable, Iterator, Callable, NamedTuple
import itertools_recipes as ir
from collections import Counter, defaultdict
from dataclasses import dataclass, field




test_input_1="""
acedgfb cdfbe gcdfa fbcad dab cefabd cdfgeb eafb cagedb ab | cdfeb fcadb cdfeb cdbaf
"""

test_input="""
be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe
edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc
fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg
fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb
aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea
fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb
dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe
bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef
egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb
gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce
"""


digit_to_word = {
    0:"abcefg",
    1:"cf",
    2:"acdeg",
    3:"acdfg",
    4:"bcdf",
    5:"abdfg",
    6:"abdefg",
    7:"acf",
    8:"abcdefg",
    9:"abcdfg", 
}

word_to_digit = {v:k for k,v in digit_to_word.items()}

word_by_size = defaultdict(list)
for k,v in word_to_digit.items():
    word_by_size[len(k)].append(v)




@dataclass
class Seven_segment:
    signal:tuple[frozenset[str],...]
    output:tuple[frozenset[str],...]
    _word_to_digit:dict[frozenset[str],int] = field(init=False, default_factory=dict)
    _output:int = None

    def __post_init__(self):
        self.signal = tuple(map(frozenset,self.signal))
        self.output = tuple(map(frozenset,self.output))
    
    def decode_output(self) -> int:
        if self._output is not None:
            return self._output
        if not self._word_to_digit:
            self.decode()
        self._output = out = sum(self._word_to_digit[c]*(10**i) for i,c in enumerate(reversed(self.output)))
        return out
    
    def decode(self):
        count = defaultdict(list)
        wtd = self._word_to_digit
        for seg in self.signal:
            count[len(seg)].append(seg)
        for size,val in [(2,1),(4,4),(3,7),(7,8)]:
            assert len(count[size])==1
            wtd[count[size][0]] = val
            wtd[val] = count[size][0]
            del count[size]
        #get 3
        for seg in count[5]:
            if seg.intersection(wtd[1]) == wtd[1]:
                wtd[3] = seg
                wtd[seg] = 3
                break
        else:#no break
            raise ValueError("no segment for 3 found")
        count[5].remove(seg)
        #get 9
        for seg in count[6]:
            if seg.intersection(wtd[3]) == wtd[3]:
                wtd[9] = seg
                wtd[seg]=9
                break
        else:
            raise ValueError("no segment for 9 found")
        count[6].remove(seg)
        #get 0
        for seg in count[6]:
            if seg.intersection(wtd[1]) == wtd[1] :
                wtd[0] = seg
                wtd[seg] = 0
                break
        else:
            raise ValueError("no segment for 0 found")                
        count[6].remove(seg)
        assert len(count[6])==1
        wtd[6] = count[6][0]
        wtd[count[6][0]] = 6
        del count[6]
        a,b = count[5] # 2 y 5 por identificar
        if a.intersection(wtd[6]) == a:
            #a==5
            wtd[5] = a
            wtd[a] = 5
            wtd[2] = b
            wtd[b] = 2
        else:
            wtd[5] = b
            wtd[b] = 5
            wtd[2] = a
            wtd[a] = 2
        


def get_raw_data(path:str="./input.txt") -> str:
    with open(path) as file:
        return file.read()

def process_data(data:str) -> Iterator[Seven_segment]:
    """transform the raw data into a procesable form"""
    for line in ir.interesting_lines(data):
        yield Seven_segment(*ir.isplit(line.split(),"|")) 
        
    

def part1(data:str) -> int:
    """part 1 of the puzzle """
    data = Counter( ir.chain.from_iterable( map(len,s.output) for s in process_data(data)))
    check = [k for k,v in word_by_size.items() if len(v)==1 ]
    return sum( data[n] for n in check )





def part2(data:str) -> int:
    """part 2 of the puzzle """
    return sum( s.decode_output() for s in process_data(data))
    
 
    
   
def test1() -> bool:
    return part1(test_input) == 26

def test2() -> bool:
    return part2(test_input_1) == 5353 and part2(test_input) == 61229




data = get_raw_data()
assert test1(),"fail test 1"
print("solution part1", part1(data)) # 
assert test2(),"fail test 2"
print("solution part2", part2(data)) # 














