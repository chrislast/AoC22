# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(4)
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

def elfduties(line):
    elves = []
    for elf in line.split(","):
        emin, emax  = elf.split("-")
        elves.append(set(range(int(emin),int(emax)+1)))
    return elves

######## Part 1 ##########
def p1(expect=2 if USING_EXAMPLE else 571):
    tot = 0
    NS.p1 = []
    for line in TEXT.splitlines():
        elf1, elf2 = elfduties(line)
        NS.p1.append([elf1, elf2])
        if len(elf2-elf1) == 0 or len(elf1-elf2) == 0:
            tot += 1
    return tot

######## Part 2 ##########
def p2(expect=4 if USING_EXAMPLE else 917):
    tot = 0
    for line in TEXT.splitlines():
        elf1, elf2 = elfduties(line)
        if len(elf2|elf1) != len(elf2)+len(elf1):
            tot += 1
    return tot

if __name__ == "__main__":
    show(p1, p2)
    viz.viz4p1(NS.p1)
    #viz.viz?p2(NS)
