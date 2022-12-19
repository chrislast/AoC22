# import our helpers
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
from types import SimpleNamespace

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__))
NS = SimpleNamespace()

# parse the input
DATA = [_ for _ in TEXT.splitlines()]

R,P,S = 1,2,3 # rock paper scissors
W,D,L = 6,3,0 # win draw lose
SCORE = {'R R':D+R, 'R P':W+P, 'R S':L+S,
         'P R':L+R, 'P P':D+P, 'P S':W+S,
         'S R':W+R, 'S P':L+P, 'S S':D+S}

def play(rules):
    total = 0
    animate = []
    for _ in DATA:
        rnd = rules[_]
        total += SCORE[rnd]
        animate.append((rnd, total))
    return total, animate

######## Part 1 ##########
def p1(expect=15 if USING_EXAMPLE else 10994):
    # A B C = rock paper scissors
    # X Y Z = rock paper scissors
    rules = {
        ('A X'):"R R", ('A Y'):"R P", ('A Z'):"R S",
        ('B X'):"P R", ('B Y'):"P P", ('B Z'):"P S",
        ('C X'):"S R", ('C Y'):"S P", ('C Z'):"S S"}
    tot, NS.p1 = play(rules)
    return tot

######## Part 2 ##########
def p2(expect=12 if USING_EXAMPLE else 12526):
    # A B C = rock paper scissors
    # X Y Z = lose draw win
    rules = {
        ('A X'):"R S", ('A Y'):"R R", ('A Z'):"R P",
        ('B X'):"P R", ('B Y'):"P P", ('B Z'):"P S",
        ('C X'):"S P", ('C Y'):"S S", ('C Z'):"S R"}
    tot, NS.p2 = play(rules)
    return tot

if __name__ == "__main__":
    show(p1, p2)
    # play rock paper scissor gif with accumulating score...
    viz.viz2p1(NS.p1)
    viz.viz2p2(NS.p2)
