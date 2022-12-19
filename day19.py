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

def is_buildable(cost,resources):
    for a,b in zip(cost,resources):
        if a>b:
            return False
    return [a-b for a,b in zip(resources,cost)]

DESCS={
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
USING_EXAMPLE = False
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
        if USING_EXAMPLE:
            desc += f"\n== Minute {turn} ==\n{turndesc}"

        resources = [res+rob for res,rob in zip(resources,robots)]
        for n in (ORE,CLAY,OBSIDIAN,GEODES):
            plural = "robot" if robots[n]==1 else "robots"
            if USING_EXAMPLE:
                desc += f"{robots[n]} {DESCS[n]} {plural} collects {robots[n]} {D2[n]}; you now have {resources[n]} {D2[n]}.\n" if robots[n] else ""

        robots = [rob+newrob for rob,newrob in zip(robots,newbots)]
        for n in (ORE,CLAY,OBSIDIAN,GEODES):
            if USING_EXAMPLE:
                desc += f"The new {DESCS[n]} robot is ready; you now have {robots[n]} of them.\n" if newbots[n] else ""

        if turn == self.TURNS:
            return resources[GEODES], robots, resources, desc

        forks = []
        a,b,c,d = robots
        ore, clay, obsidian, geodes = resources
        if spentres:=is_buildable(self.costs[GEODES],resources):
            forks.append(
                self.take_turn(
                    turn+1, robots[:], [0,0,0,1], spentres,
                    desc,
                    f"Spend {self.costs[GEODES]}, to start building a {DESCS[GEODES]} robot\n" if USING_EXAMPLE else ""))
        # halt production if we have enough stock or robots to make any robot
        if ore-2 < self.maxbots[ORE] and robots[ORE] < self.maxbots[ORE]:
            if spentres := is_buildable(self.costs[ORE],resources):
                forks.append(
                    self.take_turn(
                        turn+1, robots[:], [1,0,0,0], spentres,
                        desc,
                        f"Spend {self.costs[ORE]}, to start building a {DESCS[ORE]} robot\n" if USING_EXAMPLE else ""))
        if clay-2 < self.maxbots[CLAY] and robots[CLAY] < self.maxbots[CLAY]:
            if spentres:=is_buildable(self.costs[CLAY],resources):
                forks.append(
                    self.take_turn(
                        turn+1, robots[:], [0,1,0,0], spentres,
                        desc,
                        f"Spend {self.costs[CLAY]}, to start building a {DESCS[CLAY]} robot\n" if USING_EXAMPLE else ""))
        if obsidian-2 < self.maxbots[OBSIDIAN] and robots[OBSIDIAN] < self.maxbots[OBSIDIAN]:
            if spentres:=is_buildable(self.costs[OBSIDIAN],resources):
                forks.append(
                    self.take_turn(
                        turn+1, robots[:], [0,0,1,0], spentres,
                        desc,
                        f"Spend {self.costs[OBSIDIAN]}, to start building a {DESCS[OBSIDIAN]} robot\n" if USING_EXAMPLE else ""))
        if not is_buildable(self.costs[GEODES],resources):
            forks.append(self.take_turn(turn+1, robots[:], [0,0,0,0], resources[:],desc,"")) # do nothing (accumulate resources)
        return max(forks)

    def start(self, turns):
        Blueprint.TURNS = turns
        return self.take_turn(1, [1,0,0,0], [0,0,0,0], [0,0,0,0], f"Blueprint {self.n}\n", "")

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

######### Part 1 ##########
def p1(expect=33 if USING_EXAMPLE else 1981):
    return 0
    results = []
    BLUEPRINTS = [parse(_) for _ in TEXT]
    for bp in BLUEPRINTS:
        bpres = bp.start(24)
        results.append((bp,bpres))
        print(f"{bpres[3]} cracks {bpres[0]} geodes")
    quality = [bp.n*res[0] for bp, res in results]
    return sum(quality)

######## Part 2 ##########
def p2(expect=62 if USING_EXAMPLE else 10962):
    results = []
    BLUEPRINTS = [parse(_) for _ in TEXT][:3]
    for bp in BLUEPRINTS:
        bpres = bp.start(32)
        results.append((bp,bpres))
        print(f"{bpres[3]} cracks {bpres[0]} geodes")
    return math.product([res[0] for bp,res in results])

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
