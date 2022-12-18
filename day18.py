# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input
def parse(line):
    x,y,z = line.split(",")
    # convert to int and push them in a bit to allow a border
    return int(z)+1, int(y)+1, int(x)+1

PARSED = [parse(_) for _ in TEXT]
SZ = max(_[0] for _ in PARSED)+2
SY = max(_[1] for _ in PARSED)+2
SX = max(_[2] for _ in PARSED)+2

NEIGHBOURS = np.array(
      [[[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]],

       [[0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]],

       [[0, 0, 0],
        [0, 1, 0],
        [0, 0, 0]]], dtype="uint8")
NOT_NEIGHBOURS = np.count_nonzero(NEIGHBOURS==0)
np.set_printoptions(threshold=np.inf)
ARRAY = np.zeros((SZ,SY,SX), dtype="uint8") # 3D Array
for z,y,x in PARSED:
    ARRAY[z,y,x]=1

INSIDE = 0
ROCK = 1
OUTSIDE = 2

# add a border on all axes to mark outside space
ARRAY[0,:,:] = OUTSIDE
ARRAY[:,0,:] = OUTSIDE
ARRAY[:,:,0] = OUTSIDE
ARRAY[SZ-1,:,:] = OUTSIDE
ARRAY[:,SY-1,:] = OUTSIDE
ARRAY[:,:,SX-1] = OUTSIDE

# repeat until all outside dents are joined
for z in range(1,SZ):
    for y in range(1,SY):
        for x in range(1,SX):
            for z,y,x in ((z,y,x),(SZ-z,SY-y,SX-x)):
                if ARRAY[z,y,x] == INSIDE:
                    # if any of it's neighbours are outside it must be outside too
                    chk = ARRAY[z-1:z+2,y-1:y+2,x-1:x+2] * NEIGHBOURS
                    if np.count_nonzero(chk==OUTSIDE):
                        ARRAY[z,y,x] = OUTSIDE

######## Part 1 ##########
def p1(expect=64 if USING_EXAMPLE else 3564):
    tot=0
    for z in range(SZ):
        for y in range(SY):
            for x in range(SX):
                if ARRAY[z,y,x]==ROCK:
                    chk = ARRAY[z-1:z+2,y-1:y+2,x-1:x+2] * NEIGHBOURS
                    tot += np.count_nonzero(chk!=ROCK) - NOT_NEIGHBOURS
    return tot

######## Part 2 ##########

def p2(expect=58 if USING_EXAMPLE else 2106):
    # fill in air pockets
    for z in range(SZ):
        for y in range(SY):
            for x in range(SX):
                if ARRAY[z,y,x]==INSIDE:
                    ARRAY[z,y,x]=ROCK
    # get the new surface area
    return p1()

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
