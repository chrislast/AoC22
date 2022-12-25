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

PARSED = [int(v) for v in TEXT]
LP = len(PARSED)

def f(key, n):
    numbers = [_*key for _ in PARSED]
    indices = list(range(len(numbers)))

    for i in indices * n:
        indices.pop(j := indices.index(i))
        indices.insert((j+numbers[i]) % len(indices), i)

    zero = indices.index(numbers.index(0))
    return sum(numbers[indices[(zero+p*1000) % len(numbers)]] for p in [1,2,3])

print(f(1, 1), f(811589153, 10))

####### Part 1 ##########
# def arr(p,w):
    # return [v for _,v in sorted(zip(w,p))]

# def p1(expect=0 if USING_EXAMPLE else 0):
    # values = PARSED.copy()
    # where = list(range(LP))
    # print(arr(values,where))
    # for idx in range(LP):
        # val = values[idx]
        # pos = where[idx]
        # newidx = (pos+val+LP)%(LP)
        # if val != 0:
            # for oidx in range(LP):
                # opos = where[oidx]
                # if min(newidx,pos) <= opos <= max(newidx,pos):
                    # opos += 1 if pos > opos else -1
                # where[oidx] = opos
        # where[idx]=newidx
        # print(arr(values,where))
    # breakpoint()
    # return 0

####### Part 2 ##########
# def p2(expect=0 if USING_EXAMPLE else 0):
    # return 0

# if __name__ == "__main__":
    # show(p1, p2)
    #viz.viz?(NS)
