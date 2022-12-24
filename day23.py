# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(p2=[])

np.set_printoptions(threshold=np.inf)
H = len(TEXT)
W = len(TEXT[0])
ARR = np.vectorize(ord)(np.asarray(TEXT,dtype="c")).astype("uint8")
H,W = ARR.shape

######## Part 1 ##########
def alone(elf,elves):
    ex, ey = elf
    for x in (-1, 0, 1):
        for y in (-1, 0, 1):
            if (x,y) != (0, 0):
                if (ex+x, ey+y) in elves:
                    return False
    return True

def n(x, y, elfset, i=3):
    if (x-1, y-1) in elfset or (x, y-1) in elfset or (x+1, y-1) in elfset:
        return (x,y) if i == 0 else s(x, y, elfset, i-1)
    else:
        return x, y-1
def s(x, y, elfset, i=3):
    if (x-1, y+1) in elfset or (x, y+1) in elfset or (x+1, y+1) in elfset:
        return (x,y) if i == 0 else w(x, y, elfset, i-1)
    else:
        return x, y+1
def w(x, y, elfset, i=3):
    if (x-1, y-1) in elfset or (x-1, y) in elfset or (x-1, y+1) in elfset:
        return (x,y) if i == 0 else e(x, y, elfset, i-1)
    else:
        return x-1, y
def e(x, y, elfset, i=3):
    if (x+1, y-1) in elfset or (x+1, y) in elfset or (x+1, y+1) in elfset:
        return (x,y) if i == 0 else n(x, y, elfset, i-1)
    else:
        return x+1, y

def nextelves(elves,turn):
        elfset = set(elves)
        proposed = {}
        nextelves = []
        for elf in elves:
            if alone(elf,elves):
                nextelves.append(elf)
                continue
            proposed[elf] = [n,s,w,e][turn%4](*elf, elfset)

        for elf in list(proposed.keys()):
            pos = proposed.pop(elf)
            if pos in nextelves or pos in proposed.values():
                nextelves.append(elf) # stay
                # remove others
                for otherelf, otherpos in list(proposed.items()):
                    if otherpos == pos:
                        proposed[otherelf] = otherelf
            else:
                nextelves.append(pos)
        assert len(nextelves)==len(elves)
        return nextelves

def p1(expect=110 if USING_EXAMPLE else 4158):
    elves = list(zip(*np.nonzero(ARR==35)[::-1]))
    for turn in range(10):
        elves=nextelves(elves,turn)
    maxx = max([x for x,y in elves])
    minx = min([x for x,y in elves])
    maxy = max([y for x,y in elves])
    miny = min([y for x,y in elves])
    w = maxx-minx+1
    h = maxy-miny+1
    sz = w*h
    res = sz-len(elves)
    return res

######## Part 2 ##########
def p2(expect=20 if USING_EXAMPLE else 1014):
    elves = list(zip(*np.nonzero(ARR==35)[::-1]))
    NS.p2.append(elves)
    turn = 1
    while True:
        nelves = nextelves(elves,turn)
        turn += 1
        if elves == nelves:
            break
        elves=nelves
        NS.p2.append(elves)
    return turn


if __name__ == "__main__":
    show(p1, p2)
    viz.viz23(NS)
