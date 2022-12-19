# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import networkx as nx

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input
def parse(line):
    # Valve DR has flow rate=22; tunnels lead to valves DC, YA
    _ = line.split()
    v = _[1]
    fr = int(_[4].split("=")[1][:-1])
    vvv = "".join(_[9:])
    vvv = vvv.split(",")
    return v,fr,vvv

PARSED = [parse(_) for _ in TEXT]
PD = {node:(flow,dests) for node, flow, dests in PARSED}
OPENABLE = set([node for node in PD if PD[node][0]])
G = nx.DiGraph() # just in case one way paths exist...

G.add_nodes_from(PD.keys())
for node in G.nodes:
    G.nodes[node].update(dict(flow=PD[node][0]))
    for dest in PD[node][1]:
        G.add_edge(node,dest)
from networkx.algorithms.shortest_paths.astar import astar_path_length
import networkx.drawing.nx_pylab as nd
import matplotlib.pyplot as plt
nd.draw_networkx(G)
#plt.show()

# steps from src to dest
D = {(s,d):astar_path_length(G,s,d) for s in OPENABLE|set(["AA"]) for d in OPENABLE}

######## Part 1 ##########
def panic(room,opened,turn,tot):
    if turn>29: # too late to affect anything
        return 0, []
    oldflow = sum([PD[o][0] for o in [_[0] for _ in opened]])
    newflow = oldflow + PD[room][0]
    tot += newflow
    opened = opened + [(room,turn,newflow,tot)]
    turn += 1
    flows = []
    for valve in OPENABLE-set([_[0] for _ in opened]):
        turns = D[(room,valve)]
        moveflow = newflow*turns
        flows.append(panic(valve, opened, turn+turns, tot+moveflow))
    flows.append(((31-turn)*newflow+tot, 30, tot, opened)) # add the no movement case
    return max(flows)

def p1(expect=1651 if USING_EXAMPLE else 1850):
    return panic("AA",[],1,0)[0]

######## Part 2 ##########

MINUTES_TO_TRAIN_AN_ELEPHANT = 4

def p2(expect=1707 if USING_EXAMPLE else 2306):
    santa = panic(
        room="AA",
        opened = [],
        turn = 1 + MINUTES_TO_TRAIN_AN_ELEPHANT,
        tot = 0)

    opened_by_santa = [opened[0] for opened in santa[3]][1:]
    for valve in opened_by_santa:
        OPENABLE.remove(valve)

    # send in the elephant!
    elephant = panic(
        room = "AA",
        opened = [],
        turn = 1 + MINUTES_TO_TRAIN_AN_ELEPHANT,
        tot = 0)
    breakpoint()
    return santa[0]+elephant[0]

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
