# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(floor=0,minx=1000,maxx=0)

ARRAY = np.zeros((200,1200), dtype="uint8") # 3D Array

ROCK = ord("#")
AIR = 0
SAND = ord("o")
SOURCE = (500,0)

for line in TEXT:
    px = py = None
    for xy in line.split(" -> "):
        x,y = xy.split(",")
        x = int(x)
        y = int(y)
        if px is None:
            px, py = x,y # 1st point
        else:
            minx=min(px,x)
            maxx=max(px,x)
            miny=min(py,y)
            maxy=max(py,y)
            NS.minx=min(NS.minx,minx)
            NS.maxx=max(NS.maxx,maxx)
            NS.floor=max(NS.floor,maxy)
            ARRAY[miny:maxy+1,minx:maxx+1] = ROCK
            px = x
            py = y

NS.floor += 2

# parse the input
def parse(line):
    a,b,*c = line.split()
    return a, int(b), c

# PARSED = [parse(_) for _ in TEXT]

######## Part 1 ##########
def add_grain(arr):
    x,y = SOURCE
    while True:
        left,below,right = arr[y+1,x-1:x+2]
        if below == AIR:
            y += 1
            if y == NS.floor:    # part1 exit condition
                return False
        elif left == AIR:
            x,y = x-1,y+1
            if x < NS.minx:
                NS.minx = x
        elif right == AIR:
            x,y = x+1,y+1
            if x > NS.maxx:
                NS.maxx = x
        else:
            arr[y,x] = SAND
            if (x,y) == SOURCE:  # part2 exit condition
                return False
            return True          # sand placed successfully

def p1(expect=1298):
    arr = ARRAY.copy()
    while add_grain(arr):
        pass
    NS.p1 = arr, NS.floor, NS.minx, NS.maxx
    return np.count_nonzero(arr == SAND)


######## Part 2 ##########
def p2(expect=25585):
    arr = ARRAY.copy()
    # add a floor
    arr[NS.floor,:] = ROCK
    while add_grain(arr):
        pass
    NS.p2 = arr, NS.floor, NS.minx, NS.maxx
    return np.count_nonzero(arr == SAND)

if __name__ == "__main__":
    show(p1, p2)
    viz.viz14(NS)
