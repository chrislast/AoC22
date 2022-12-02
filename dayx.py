# import our helpers
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__))
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input
try:
    DATA = [int(txt) for txt in TEXT.splitlines()]
except:
    pass

######## Part 1 ##########
def p1(expect=0):
    breakpoint()
    return 0

######## Part 2 ##########
def p2(expect=0):
    return 0

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
