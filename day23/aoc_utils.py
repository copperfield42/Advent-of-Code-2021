# https://adventofcode.com/2021/day/23
from __future__ import annotations

from typing import Iterator, Iterable, NamedTuple, Literal, Any
import itertools_recipes as ir
from aoc_recipes import mirror_dict, get_raw_data, shortest_path_grafo


test_input = """
#############
#...........#
###B#C#B#D###
  #A#D#C#A#
  #########
"""

ENERGY = {
    "A": 1,
    "B": 10,
    "C": 100,
    "D": 1000,
}
PLACES = {
    "A": 1,
    "B": 2,
    "C": 3,
    "D": 4,
    ".": -1
}

PLACES = mirror_dict(PLACES)

class Amphipod(NamedTuple):
    halway: str
    room1: str
    room2: str
    room3: str
    room4: str
    cost: int = 0

    def __str__(self):
        parts = [ "#"*13, f"#{self.halway}#" ]
        extra = True
        for r1, r2, r3, r4 in zip(*self[1:-1]):
            parts.append(f"  #{r1}#{r2}#{r3}#{r4}#  ")
            if extra:
                parts[-1] = parts[-1].replace(" ", "#")
                extra = False
        parts.append("  " + ("#"*9) + "  ")
        parts.append(f"energy = {self.cost}")
        return "\n".join(parts)

    def is_room_empty(self, room: int) -> bool:
        return all(x == "." for x in self[room])

    def is_room_finalize(self, room: int) -> bool:
        return all(x == PLACES[room] for x in self[room])

    def is_room_ready(self, room: int) -> int:
        if all(x in (PLACES[room], ".") for x in self[room]):
            return self[room].count(".")
        else:
            return -1

    def pop_from_room(self, room: int) -> tuple[int, str, str]:
        old = self[room]
        for i, c in enumerate(old):
            if c != ".":
                break
        poped = old[i]
        new = "".join(c if j != i else "." for j, c in enumerate(old))
        return i, poped, new

    def fill_room(self, room: int) -> str:
        old = self[room]
        i = max((i for i, c in enumerate(old) if c == "."), default=-1)
        if i == -1:
            return old
        return "".join(c if j != i else PLACES[room] for j, c in enumerate(old))

    def is_done(self) -> bool:
        return all(self.is_room_finalize(i) for i in range(1, 5))


def sub_move(state: Amphipod, start: int, direction: Literal[1, -1], new_room: str, new_room_pos: int, amph: str, steps: int) -> Iterator[Amphipod]:
    room = PLACES[amph]
    rooms = list(state[:-1])
    rooms[new_room_pos] = new_room
    for i in range(start, len(state.halway) if direction == 1 else direction, direction):
        if state.halway[i] == ".":
            steps += 1
            if i in (2, 4, 6, 8):
                if i == 2*room:
                    extra_steps = -1
                    if state.is_room_empty(room):
                        extra_steps = len(state[room])
                    if (space := state.is_room_ready(room)) > 0:
                        extra_steps = space
                    if extra_steps != -1:
                        # enter the room
                        steps += extra_steps
                        halway = list(state.halway)
                        halway[i] = "."
                        rooms[0] = "".join(halway)
                        rooms[room] = state.fill_room(room)
                        yield Amphipod(*rooms, cost=state.cost + ENERGY[amph] * steps)
                        return
                continue
            halway = list(state.halway)
            halway[i] = amph
            rooms[0] = "".join(halway)
            yield Amphipod(*rooms, cost=state.cost + ENERGY[amph] * steps)
        else:
            return


def go_to_room(state: Amphipod, amph: str, pos: int) -> Amphipod | None:
    P = PLACES[amph]
    steps = 0
    if state.is_room_empty(P):
        steps += len(state[P])
    elif (space := state.is_room_ready(P)) > 0:
        steps += space
    else:
        return
    direc: int = 1 if pos <= (2 * P) else (-1)
    old_pos = pos
    while pos != (2*P):
        if state.halway[pos + direc] != ".":
            return
        pos += direc
        steps += 1
    halway = list(state.halway)
    halway[old_pos] = "."
    new_state = ["".join(halway), *state[1:]]
    new_state[P] = state.fill_room(P)
    new_state[-1] += ENERGY[amph]*steps
    return Amphipod(*new_state)


def move(state: Amphipod, grafo: Any = None) -> Iterator[Amphipod]:
    for room in range(1, 5):
        if state.is_room_ready(room) >= 0:
            continue
        steps, A, new_room = state.pop_from_room(room)
        start = 2 * room
        direc: Literal[1, -1]
        for direc in (1, -1):
            yield from sub_move(state, start, direc, new_room, room, A, steps)
    for amph in "ABCD":
        if amph in state.halway:
            for i, a in enumerate(state.halway):
                if a == amph:
                    room = go_to_room(state, amph, i)
                    if room:
                        yield room


def process_data(data: str) -> ...:
    """transform the raw data into a procesable form"""
    R1: str
    R2: str
    _, _, R1, R2, *_ = ir.interesting_lines(data)
    R1 = R1.replace("#", "")
    R2 = R2.replace("#", "")
    return Amphipod("."*11, *map("".join, zip(R1, R2)))
    
    
GOAL = Amphipod("."*11, "AA", "BB", "CC", "DD")[:-1]


def cost(old: Amphipod, new: Amphipod, old_cost: int, grafo: Any) -> int:
    return new.cost


def shortest_path_amphipod(initial: Amphipod) -> int:
    return shortest_path_grafo(initial, Amphipod.is_done, initial, move, cost, 0)[0]


def manual_mode(data: str):
    start = process_data(data)
    current = start
    while not current.is_done():
        next_move = list(move(current))
        print(current)
        print("Pick next move")
        for i, m in enumerate(next_move):
            print(f"{i})")
            print(m)
        index = int(input("your choice: "))
        current = next_move[index]
        print("\n\n")
    print("done")

