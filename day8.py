# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

MAP=Map(TEXT)
W,H = MAP.img.size

V = set() # set of visible trees

# parse the input
try:
    DATA = [int(txt) for txt in TEXT.splitlines()]
except:
    DATA = Map(TEXT)

######## Part 1 ##########
def p1(expect=1733):
    visible = set() # no duplicates please

    # look from top and bottom edges
    for x in range(0,W):
        thmax = 0
        for y in range(0,H):
            if MAP.get((x,y)) > thmax:
                visible.add((x,y))
                thmax = MAP.get((x,y))
        thmax = 0
        for y in range(H-1,-1,-1):
            if MAP.get((x,y)) > thmax:
                visible.add((x,y))
                thmax = MAP.get((x,y))

    # look from left and right edges
    for y in range(0,H):
        thmax = 0
        for x in range(0,W):
            if MAP.get((x,y)) > thmax:
                visible.add((x,y))
                thmax = MAP.get((x,y))
        thmax = 0
        for x in range(W-1,-1,-1):
            if MAP.get((x,y)) > thmax:
                visible.add((x,y))
                thmax = MAP.get((x,y))

    NS.visible = visible
    return len(visible)

######## Part 2 ##########
def score(tx,ty,tz):
    u=d=l=r=0
    for x in range(tx+1,W): # look right
        r+=1
        if MAP.get((x,ty)) >= tz:
            break
    for x in range(tx-1,-1,-1): # look left
        l+=1
        if MAP.get((x,ty)) >= tz:
            break
    for y in range(ty+1,H): # look down
        d+=1
        if MAP.get((tx,y)) >= tz:
            break
    for y in range(ty-1,-1,-1): # look up
        u+=1
        if MAP.get((tx,y)) >= tz:
            break
    # print(tx,ty,hex(tz),u,l,d,r)
    return u*l*d*r


def p2(expect=284648):
    smax = 0
    for x in range(W):
        for y in range(H):
            val = score(x,y,MAP.get((x,y)))
            if val > smax:
                NS.treehouse = (x,y)
                smax = val
    return smax

if __name__ == "__main__":
    show(p1, p2)
    viz.viz8p2(NS, MAP)
    viz.viz8p1(NS, MAP)
