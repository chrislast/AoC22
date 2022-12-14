# import our helpers
import sys
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
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY).show()

ROCK = ord("#")
AIR = ord(".")
_SOURCE = ord("+")
SAND = ord("o")
SOURCE = (500,0)
ARRAY.fill(AIR)

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
def add_grain(arr, part2=False):
    x,y = SOURCE
    while True:
        left,below,right = arr[y+1,x-1:x+2]
        if below == AIR:
            y+=1
            if y == NS.floor: # part1 exit condition
                return False
        elif left == AIR:
            y+=1
            x-=1
            NS.minx=min(NS.minx,x)
        elif right == AIR:
            x+=1
            y+=1
            NS.maxx=max(NS.maxx,x)
        else:
            arr[y,x] = SAND
            if part2 and (x,y) == SOURCE:
                return False
            return True

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
    while add_grain(arr,True):
        pass
    NS.p2 = arr, NS.floor, NS.minx, NS.maxx
    return np.count_nonzero(arr == SAND)

if __name__ == "__main__":
    show(p1, p2)
    array, floor, minx, maxx = NS.p1
    m=Map(array[:floor+2,minx-1:maxx+2])
    w,h = m.img.size
    m.img.resize((w*3,h*3)).save(Path(__file__).parent / 'output' / 'day14a.png')
    array, floor, minx, maxx = NS.p2
    m=Map(array[:floor+2,minx-1:maxx+2])
    w,h = m.img.size
    m.img.resize((w*3,h*3)).save(Path(__file__).parent / 'output' / 'day14b.png')
