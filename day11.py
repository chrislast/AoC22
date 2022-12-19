# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
from collections import deque
import math

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

INPUT_GROUPS = [TEXT[n:n+6] for n in range(0,len(TEXT),7)]

class Monkey:
    def __init__(self, txt):
        self.n = int(txt[0][7:-1])
        i = txt[1][18:].replace(" ","").split(",")
        self.items = deque([int(_) for _ in i])
        self.operation = txt[2][23:].split()
        try: # convert constant value
            self.operation[1] = int(self.operation[1])
        except: 
            pass # value is "old"
        self.divisible_by = int(txt[3][21:])
        self.iftrue = int(txt[4][29:])
        self.iffalse = int(txt[5][30:])
        self.inspects = 0

    def monkey_around(self):
        while self.items:
            self.inspects += 1 # count inspections for solution
            item = self.items.popleft() 

            # increase worry
            match self.operation:
                case ["+", "old"]: item += item
                case ["*", "old"]: item *= item
                case ["+", x]:     item += x
                case ["*", x]:     item *= x

            # reduce worry
            try:
                item %= Monkey.lcm  # monkeypatched in part 2 only
            except AttributeError:
                item //= 3  # part 1 behaviour

            # throw item to new monkey
            if item % self.divisible_by:
                Monkey.monkeys[self.iffalse].items.append(item)
            else:
                Monkey.monkeys[self.iftrue].items.append(item)

    def __str__(self):
        return f"Monkey {self.n}: {self.items}"

######## Part 1 ##########
def monkey_business_after_playing_rounds(rounds):
    for _ in range(rounds):
        for monkey in Monkey.monkeys:
            monkey.monkey_around()
    monkey_business = math.prod(sorted([m.inspects for m in Monkey.monkeys])[-2:])
    return monkey_business

def p1(expect=10605 if USING_EXAMPLE else 69918):
    Monkey.monkeys = [Monkey(monkey_info) for monkey_info in INPUT_GROUPS]
    return monkey_business_after_playing_rounds(20)

######## Part 2 ##########
def p2(expect=2713310158 if USING_EXAMPLE else 19573408701):
    Monkey.monkeys = [Monkey(monkey_info) for monkey_info in INPUT_GROUPS]
    # calculate a divisor to use on `worry` which won't affect monkey selection by
    # finding the lowest common multiple of all monkeys' divisible_by test values
    Monkey.lcm = math.lcm(*[m.divisible_by for m in Monkey.monkeys])
    return monkey_business_after_playing_rounds(10_000)

if __name__ == "__main__":
    show(p1, p2)
