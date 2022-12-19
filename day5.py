# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TXT = load(day(__file__)).splitlines()
NDOCKS = 9 if len(TXT)>20 else 3
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(p1=[],p2=[])

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
def p1(expect="CMZ" if USING_EXAMPLE else "VJSFHWGFT"):
    docks=DOCKS[:]
    for n,src,tgt in COMMANDS:
        docks[tgt] = docks[src][:n][::-1]+docks[tgt]
        docks[src] = docks[src][n:]
        NS.p1.append(docks)
    return "".join(_[0] for _ in docks)

######## Part 2 ##########
def p2(expect="MCD" if USING_EXAMPLE else "LCTQFBVZV"):
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
