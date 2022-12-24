# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np
import math
from collections import deque

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

np.set_printoptions(threshold=np.inf)
H = len(TEXT)
W = len(TEXT[0])
ARR = np.asarray(TEXT,dtype="c")
H,W = ARR.shape

ENTRY = (1, 0)
EXIT = (W-2, H-1)

# initialize wind sets
BLIZU = set((x,y) for y,x in zip(*np.where(ARR==b"^")))
BLIZD = set((x,y) for y,x in zip(*np.where(ARR==b"v")))
BLIZR = set((x,y) for y,x in zip(*np.where(ARR==b">")))
BLIZL = set((x,y) for y,x in zip(*np.where(ARR==b"<")))

WIND_REPEATS = math.lcm(H-2,W-2)
WINDS = {}
# pre-calculate all the possible sets of wind as a single set
for i in range(WIND_REPEATS):
    WINDS[i] = BLIZU | BLIZR | BLIZL | BLIZD
    BLIZU = set((x, (y-2)%(H-2)+1   ) for x,y in BLIZU)
    BLIZD = set((x,   (y)%(H-2)+1   ) for x,y in BLIZD)
    BLIZR = set((     (x)%(W-2)+1, y) for x,y in BLIZR)
    BLIZL = set((   (x-2)%(W-2)+1, y) for x,y in BLIZL)

######## Part 1 ##########

def bfs(start,finish,turn):
    seen = set()
    bfs = deque([(start,turn)])
    while bfs:
        pos, turn = bfs.popleft()
        if pos == finish:
            break
        if (pos,turn) in seen:
            continue
        seen.add((pos,turn))
        x,y = pos
        turn += 1
        wind = WINDS[turn%WIND_REPEATS]

        for dx,dy in ((0,0),(1,0),(-1,0),(0,1),(0,-1)):
            if (0 < x+dx < W-1 and 0 < y+dy < H-1 and (x+dx,y+dy) not in wind) or (x+dx,y+dy) == start or (x+dx,y+dy) == finish:
                bfs.append(((x+dx,y+dy), turn))
    return turn

def p1(expect=18 if USING_EXAMPLE else 247):
    return bfs(ENTRY, EXIT, 0)

######## Part 2 ##########

def p2(expect=54 if USING_EXAMPLE else 728):
    there = bfs(ENTRY, EXIT, 0)
    back =  bfs(EXIT, ENTRY, there)
    there_again = bfs(ENTRY, EXIT, back)
    return there_again

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
