# import our helpers
import sys
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(4)
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

if len(sys.argv) > 1:
 TEXT = """2-4,6-8
2-3,4-5
5-7,7-9
2-8,3-7
6-6,4-6
2-6,4-8
"""

def elfduties(line):
    elves = []
    for elf in line.split(","):
        emin, emax  = elf.split("-")
        elves.append(set(range(int(emin),int(emax)+1)))
    return elves

######## Part 1 ##########
def p1(expect=571):
    tot = 0
    for line in TEXT.splitlines():
        elf1, elf2 = elfduties(line)
        if len(elf2-elf1) == 0 or len(elf1-elf2) == 0:
            tot += 1
    return tot

######## Part 2 ##########
def p2(expect=917):
    tot = 0
    for line in TEXT.splitlines():
        elf1, elf2 = elfduties(line)
        if len(elf2|elf1) != len(elf2)+len(elf1):
            tot += 1
    return tot

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
