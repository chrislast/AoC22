# import our helpers
import sys
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TXT = load(day(__file__)).splitlines()
NDOCKS = 9
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(p1=[],p2=[])

if len(sys.argv) > 1:
    # Use test data instead
    NDOCKS = 3
    TXT = """
    [D]     
[N] [C]     
[Z] [M] [P]  
 1   2   3  

move 1 from 2 to 1
move 3 from 1 to 3
move 2 from 2 to 1
move 1 from 1 to 2
""".splitlines()[1:]

# parse initial dock setup
DOCKS = [""]*NDOCKS
for line in TXT:
    if line.startswith(" 1 "):
        break
    for _ in range(NDOCKS):
        i = _*4+1
        if line[i] != " ":
            DOCKS[_] += line[i]

# parse commands
CMDTXT=[_ for _ in TXT if _.startswith("move")]
COMMANDS = []
for cmd in CMDTXT:
    _ = cmd.split(" ")
    COMMANDS.append([int(_[1]),int(_[3])-1,int(_[5])-1])

######## Part 1 ##########
def p1(expect="VJSFHWGFT"):
    docks=DOCKS[:]
    for n,src,tgt in COMMANDS:
        docks[tgt] = docks[src][:n][::-1]+docks[tgt]
        docks[src] = docks[src][n:]
        NS.p1.append(docks)
    return "".join(_[0] for _ in docks)

######## Part 2 ##########
def p2(expect="LCTQFBVZV"):
    docks=DOCKS[:]
    for n,src,tgt in COMMANDS:
        docks[tgt] = docks[src][:n]+docks[tgt]
        docks[src] = docks[src][n:]
        NS.p1.append(docks)
    return "".join(_[0] for _ in docks)

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
