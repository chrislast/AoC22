# import our helpers
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
from collections import Counter
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__))
NS = SimpleNamespace()

######## Part 1 ##########
def p1(answer=67016):
    """elf with most food"""
    NS.elves = []
    elf_calories = 0
    for calories in TEXT.splitlines():
        if calories:
            elf_calories += int(calories)
        else:
            NS.elves.append(elf_calories)
            elf_calories = 0
    return max(NS.elves)

######## Part 2 ##########
def p2(answer=200116):
    return sum(sorted(NS.elves)[-3:])

if __name__ == "__main__":
    show(p1, p2)
    viz.viz1a(NS.elves)
    viz.viz1b(NS.elves)
