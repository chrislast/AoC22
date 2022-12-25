# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()

def tosnafu(val):
    acc = []
    while val:
        d,m = divmod(val,5)
        if m<3:
            acc.append(str(m))
        else:
            d += 1
            acc.append("=" if m==3 else "-")
        val = d
    return "".join(acc[::-1])

def fromsnafu(txt):
    acc = []
    for char in txt:
        match char:
            case "0": acc.append(0)
            case "1": acc.append(1)
            case "2": acc.append(2)
            case "-": acc.append(-1)
            case "=": acc.append(-2)
    multiplier = 1
    result = 0
    for value in acc[::-1]:
        result += value * multiplier
        multiplier *= 5
    return result

######## Part 1 ##########
def p1(expect="2=-1=0" if USING_EXAMPLE else "2-21=02=1-121-2-11-0"):
    fuel_reqs = [fromsnafu(t) for t in TEXT]
    return tosnafu(sum(fuel_reqs))

######## Part 2 ##########
def p2(expect=0 if USING_EXAMPLE else 0):
    return 0

if __name__ == "__main__":
    show(p1, p2)
