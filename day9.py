# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
PARSED = [_.split() for _ in TEXT]
PARSED = [(d,int(n)) for d,n in PARSED]
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(viz=[])

DIR2XY = {"U": (0,1), "D": (0,-1), "L": (-1,0), "R": (1,0)}

######## Part 1 ##########

def sign(n):
    """negative returns -1, zero returns 0, positive returns 1"""
    if n==0:
        return 0
    return 1 if n>0 else -1

def is_touching(hx,hy,tx,ty):
    """identical, adjacent or diagonal are all 'touching'"""
    return max(abs(hx-tx),abs(hy-ty)) < 2

def update_knot(headmost, tailmost):
    ((hx,hy),(tx,ty)) = headmost, tailmost
    if not is_touching(hx,hy,tx,ty):
        tx += sign(hx-tx)
        ty += sign(hy-ty)
    return tx,ty

def rope_tail_positions(knots):
    # rope[0] is the head .. rope[-1] is the tail
    NS.viz.append([]) # visualization use
    rope = [(0,0)] * knots
    tail_visited = set(rope)
    for direction, steps in PARSED:
        dx, dy = DIR2XY[direction]
        for _ in range(steps):
            # update the head of the ropes position
            rope[0] = (rope[0][0]+dx, rope[0][1]+dy)
            # update each knot after head sequentially
            for knot in range(len(rope)-1):
                rope[knot+1] = update_knot(rope[knot],rope[knot+1])
            # add the final tail position to visited list
            tail_visited.add(rope[-1])
        NS.viz[-1].append(rope.copy()) # store rope for visualization use
    return tail_visited

def p1(expect=88 if USING_EXAMPLE else 5695):
    return len(rope_tail_positions(knots=2))

######## Part 2 ##########

def p2(expect=36 if USING_EXAMPLE else 2434):
    return len(rope_tail_positions(knots=10))

if __name__ == "__main__":
    show(p1, p2)
    viz.viz9p1(NS.viz[0])
    viz.viz9p2(NS.viz[1])
