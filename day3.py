# import our helpers
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

def pri(c):
    if "A" <= c <= "Z":
        return ord(c)-ord('A')+27
    return ord(c)-ord('a')+1

######## Part 1 ##########
def p1(expect=157 if USING_EXAMPLE else 7997):
    tot = 0
    for backpack in TEXT:
        sz = len(backpack)//2
        c = (set(backpack[:sz]) & set(backpack[sz:])).pop()
        tot += pri(c)          
    return tot

######## Part 2 ##########
def p2(expect=70 if USING_EXAMPLE else 2545):
    tot = 0
    for i in range(0,len(TEXT),3):
        grp = TEXT[i:i+3]
        eb1,eb2,eb3 = map(set,grp)
        c=(eb1&eb2&eb3).pop()
        tot += pri(c)            
    return tot


if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
