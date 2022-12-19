# import our helpers
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
from collections import Counter
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__))
NS = SimpleNamespace()

######## Part 1 ##########
def p1(answer=24000 if USING_EXAMPLE else 67016):
    """elf with most food"""
    NS.elves = [0]
    for calories in TEXT.splitlines():
        if calories:
            NS.elves[-1] += int(calories)
        else:
            NS.elves.append(0)
    return max(NS.elves)

######## Part 2 ##########
def p2(answer=45000 if USING_EXAMPLE else 200116):
    return sum(sorted(NS.elves)[-3:])

if __name__ == "__main__":
    show(p1, p2)
    viz.viz1p1(NS.elves)
    viz.viz1p2(NS.elves)
