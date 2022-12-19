# import our helpers
import sys
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
from collections import deque, namedtuple

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

MAP=Map(TEXT) # load 2D map with elevations
W,H = MAP.img.size

# parse map
for x in range(W):
    for y in range(H):
        p = MAP.get((x,y))
        if p == ord("S"):
            START=(x,y)         # found START
            MAP.set(START,"a")  # replace with elevation a on map
        elif p == ord("E"):
            END=(x,y)           # found END
            MAP.set(END,"z")    # replace with elevation z on map

NODE = namedtuple("BFSnode", "x y z steps route")
NS.map = MAP

######## Part 1 ##########
def p1(expect=31 if USING_EXAMPLE else 504):
    """climb the hill using breadth-first search to reach target position"""
    BFS = deque([NODE(*START, ord("a"), 0, [START])])
    VISITED = set([START])
    while BFS:
        pos = BFS.popleft()
        if (pos.x, pos.y) == END:
            break
        for new_xy in ((pos.x-1,pos.y),(pos.x+1,pos.y),(pos.x,pos.y-1),(pos.x,pos.y+1)):
            new_x, new_y = new_xy
            if 0<=new_x<W and 0<=new_y<H:
                new_z = MAP.get(new_xy)
                if new_xy not in VISITED and new_z <= pos.z+1:
                    VISITED.add(new_xy)
                    new_route=pos.route.copy()
                    new_route.append(new_xy)
                    BFS.append(NODE(new_x, new_y, new_z, pos.steps+1, new_route))
    NS.p1 = pos.route
    return pos.steps

######## Part 2 ##########
def p2(expect=29 if USING_EXAMPLE else 500):
    """descend hill using breadth-first search to reach target elevation"""
    BFS = deque([NODE(*END, ord("z"), 0, [END])])
    VISITED = set([END])
    while BFS:
        pos = BFS.popleft()
        if pos.z == ord("a"):
            break
        for new_xy in ((pos.x-1,pos.y),(pos.x+1,pos.y),(pos.x,pos.y-1),(pos.x,pos.y+1)):
            new_x, new_y = new_xy
            if 0<=new_x<W and 0<=new_y<H:
                new_z = MAP.get(new_xy)
                if new_xy not in VISITED and new_z >= pos.z-1:
                    VISITED.add(new_xy)
                    new_route=pos.route.copy()
                    new_route.append(new_xy)
                    BFS.append(NODE(new_x, new_y, new_z, pos.steps+1, new_route))
    NS.p2 = pos.route
    return pos.steps

if __name__ == "__main__":
    show(p1, p2)
    viz.viz12p1(NS)
    viz.viz12p2(NS)
