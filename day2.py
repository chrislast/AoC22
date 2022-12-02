# import our helpers
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__))
NS = SimpleNamespace()

# parse the input
NS.DATA = [tuple(_.split()) for _ in TEXT.splitlines()]

######## Part 1 ##########
def p1(expect=10994):
    tot = 0
    # lose=0, draw=3, win=6
    # choice: A/X/rock=1, B/Y/paper=2, C/Z/scissors=3
    NS.score1 = {
        ('A','X'):3+1, ('A','Y'):6+2, ('A','Z'):0+3,
        ('B','X'):0+1, ('B','Y'):3+2, ('B','Z'):6+3,
        ('C','X'):6+1, ('C','Y'):0+2, ('C','Z'):3+3}
    for _ in NS.DATA:
        tot += NS.score1[_]
    return tot

######## Part 2 ##########
def p2(expect=12526):
    tot = 0
    # outcome: X/lose=0, Y/draw=3, Z/win=6
    # rock=1, paper=2, scissors=3
    NS.score2 = {
        ('A','X'):3+0, ('A','Y'):1+3, ('A','Z'):2+6,
        ('B','X'):1+0, ('B','Y'):2+3, ('B','Z'):3+6,
        ('C','X'):2+0, ('C','Y'):3+3, ('C','Z'):1+6}
    for _ in NS.DATA:
        tot += NS.score2[_]
    return tot


if __name__ == "__main__":
    show(p1, p2)
    # play rock paper scissor gif with accumulating score...
    #viz.viz2p1(NS)
    #viz.viz2p2(NS)
