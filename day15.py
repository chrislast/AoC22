# import our helpers
import sys
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, using_example
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY).show()

# parse the input
def parse(line):
    # Sensor at x=2391367, y=3787759: closest beacon is at x=2345659, y=4354867
    n = line.split()
    x1=int(n[2].split("=")[1][:-1])
    y1=int(n[3].split("=")[1][:-1])
    x2=int(n[8].split("=")[1][:-1])
    y2=int(n[9].split("=")[1])
    return (x1,y1),(x2,y2)

def dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return (max(x1,x2)-min(x1,x2))+(max(y1,y2)-min(y1,y2))

class Sensor:
    def __init__(self, spos, bpos):
        self.pos = spos
        self.beacon = bpos
        self.dist = dist(spos,bpos)
        self.minx = spos[0]-self.dist
        self.maxx = spos[0]+self.dist

    def covered(self, pos):
        """pos is covered by this beacon"""
        return dist(pos,self.pos) <= self.dist

    def next_unknown_x(self, pos):
        # If this beacon covers pos return the next pos.x for pos.y
        # which it doesn't so we can skip a lot of x value tests
        x,y=pos
        px,py = self.pos
        if self.covered(pos):
            ydist = max(y,py)-min(y,py)
            xoff = x-px
            xdist = self.dist-ydist-xoff
            return x+xdist+1 # next uncovered x
        else:
            return x # not known by this beacon


PARSED = [parse(_) for _ in TEXT]
SENSORS = [Sensor(spos,bpos) for spos,bpos in PARSED]
BEACONS = [bpos for _,bpos in PARSED]
MAXX = max([sensor.maxx for sensor in SENSORS])
MINX = min([sensor.minx for sensor in SENSORS])

######## Part 1 ##########
def p1(expect=4424278):
    """painful brute force"""
    covered = 0
    y = 10 if using_example() else 2_000_000
    for x in range(MINX,MAXX+1):
        if (x,y) not in BEACONS:
            if any(s.covered((x,y)) for s in SENSORS):
                covered += 1
    return covered

######## Part 2 ##########
def p2(expect=10382630753392):
    """smart brute force"""
    x,y = (0,0)
    r = 20 if using_example() else 4_000_000
    while y <= r:
        while x <= r:
            cmpx = x
            for s in SENSORS:
                x = s.next_unknown_x((x,y))
                if x > r:
                    break
            if x == cmpx:
                return x*4_000_000+y
        x,y = (0, y+1)
    raise RuntimeError("No solution found!")

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
