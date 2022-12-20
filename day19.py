# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np
import math

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

ORE = 0
CLAY = 1
OBSIDIAN = 2
GEODES = 3

# parse the input
def parse(line):
    #Blueprint 30:
    # Each ore robot costs 4 ore.
    # Each clay robot costs 3 ore.
    # Each obsidian robot costs 2 ore and 20 clay.
    # Each geode robot costs 3 ore and 9 obsidian.
    words = line.split()
    bpn = int(words[1][:-1])
    orc = int(words[6])
    clc = int(words[12])
    obo = int(words[18])
    obc = int(words[21])
    geo = int(words[27])
    gob = int(words[30])
    return Blueprint(bpn, ((orc,0,0,0),(clc,0,0,0),(obo,obc,0,0),(geo,0,gob,0)))

def is_buildable(cost,resources):
    for a,b in zip(cost,resources):
        if a>b:
            return False
    return [a-b for a,b in zip(resources,cost)]

D1={
    0: "ore-collecting",
    1: "clay-collecting",
    2: "obsidian-collecting",
    3: "geode-cracking"
}

D2={
    0: "ore",
    1: "clay",
    2: "obsidian",
    3: "geodes"
}

SHOW_COMMENTARY = False

class Blueprint:
    TURNS = 0
    def __init__(self, n, costs):
        self.n = n
        self.costs = costs
        # no need to make more of a robot once you can make any robot
        self.maxbots = [max(_[n] for _ in self.costs) for n in range(4)]
        self.maxbots[3] = self.TURNS
        self.lookup = {}

    def take_turn(self,turn,robots,newbots,resources,desc,turndesc):
        # mine stuff
        if SHOW_COMMENTARY:
            desc += f"\n== Minute {turn} ==\n{turndesc}"

        resources = [res+rob for res,rob in zip(resources,robots)]
        for n in (ORE,CLAY,OBSIDIAN,GEODES):
            plural = "robot" if robots[n]==1 else "robots"
            if SHOW_COMMENTARY:
                desc += f"{robots[n]} {D1[n]} {plural} collects {robots[n]} {D2[n]}; you now have {resources[n]} {D2[n]}.\n" if robots[n] else ""

        robots = [rob+newrob for rob,newrob in zip(robots,newbots)]
        for n in (ORE,CLAY,OBSIDIAN,GEODES):
            if SHOW_COMMENTARY:
                desc += f"The new {D1[n]} robot is ready; you now have {robots[n]} of them.\n" if newbots[n] else ""

        if turn == self.TURNS:
            return resources[GEODES], robots, resources, desc

        #
        forks = []

        # always make a geode cracker if one is available
        if spentres:=is_buildable(self.costs[GEODES],resources):
            forks.append(
                self.take_turn(
                    turn+1, robots.copy(), [0,0,0,1], spentres, desc, f"Spend {self.costs[GEODES]}, to start building a {D1[GEODES]} robot\n" if SHOW_COMMENTARY else ""))

        # otherwise try doing nothing and accumulating resources to build a better robot
        else:
            forks.append(self.take_turn(turn+1, robots.copy(), [0,0,0,0], resources.copy(), desc, ""))

        # and also try making any robot we have resources for
        for rtype, newbot in zip((ORE,       CLAY,      OBSIDIAN),
                                 ((1,0,0,0), (0,1,0,0), (0,0,1,0))):
            # halt production of a robot type if we (probably) have enough stock or robots to make any robot
            if resources[rtype]-2 < self.maxbots[rtype] and robots[rtype] < self.maxbots[rtype]:
                if spentres := is_buildable(self.costs[rtype], resources):
                    forks.append(self.take_turn(turn+1, robots.copy(), newbot, spentres, desc, f"Spend {self.costs[rtype]}, to start building a {D1[rtype]} robot\n" if SHOW_COMMENTARY else ""))

        # return the startegy that yielded most geodes
        return max(forks)

    def start(self, turns):
        Blueprint.TURNS = turns
        return self.take_turn(
            turn = 1,
            robots = [1,0,0,0],
            newbots = [0,0,0,0],
            resources = [0,0,0,0],
            desc = f"Blueprint {self.n}\n",
            turndesc = "")

######### Part 1 ##########
def p1(expect=33 if USING_EXAMPLE else 1981):
    results = []
    BLUEPRINTS = [parse(_) for _ in TEXT]
    for bp in BLUEPRINTS:
        bpres = bp.start(turns=24)
        results.append((bp,bpres))
        print(f"{bpres[3]} cracks {bpres[0]} geodes")
    quality = [bp.n*res[0] for bp, res in results]
    return sum(quality)

######## Part 2 ##########
def p2(expect=62 if USING_EXAMPLE else 10962):
    results = []
    BLUEPRINTS = [parse(_) for _ in TEXT][:3]
    for bp in BLUEPRINTS:
        bpres = bp.start(turns=32)
        results.append((bp, bpres))
        print(f"{bpres[3]} cracks {bpres[0]} geodes")
    return math.prod([res[0] for bp,res in results])

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
