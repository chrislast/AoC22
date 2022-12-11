# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TXT = load(day(__file__))
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(p1=[],p2=[])

######## Part 1 ##########
def p1(expect=1140):
    sz=4
    for i in range(len(TXT)):
        if len(set(TXT[i:i+sz])) == sz:
            return i+sz

######## Part 2 ##########
def p2(expect=3495):
    sz=14
    for i in range(len(TXT)):
        if len(set(TXT[i:i+sz])) == sz:
            return i+sz

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
