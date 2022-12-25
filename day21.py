# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np
from copy import deepcopy

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

# parse the input
def parse(line):
    inst = []
    match line.split():
        case n, lhs, op, rhs:
           inst.append([0, n[:-1], lhs, op, rhs])
        case n, val:
            inst.append([1, n[:-1], int(val)])
    return inst

PARSED = [parse(_) for _ in TEXT]

# np.set_printoptions(threshold=np.inf)
# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY).show() # draw

# from networkx.algorithms.shortest_paths.astar import astar_path_length
# import networkx.drawing.nx_pylab as nd
# import matplotlib.pyplot as plt
# G = nx.DiGraph() # just in case one way paths exist...
# G.add_nodes_from(listofstring?)
# for node in G.nodes:
#     G.nodes[node].update(dict(property=val))
#     for dest in listofdestnodes:
#         G.add_edge(node,dest)
# nd.draw_networkx(G) # show network
# plt.show() # draw


OP={"+": lambda x,y:x+y,
    "-": lambda x,y:x-y,
    "/": lambda x,y:x//y,
    "*": lambda x,y:x*y}

######## Part 1 ##########
def p1(expect=152 if USING_EXAMPLE else 145167969204648):
    known = {}
    unknown = {}
    for line in PARSED:
        match line[0]:
            case 0, xname, xlhs, xop, xrhs:
                unknown[xname] = [xlhs,xop,xrhs]
            case 1, xname, val:
                known[xname] = val
    while True:
        monkeys = list(unknown.keys())
        for monkey in monkeys:
            m = unknown[monkey]
            lm, op, rm = m
            if lm in known:
                m[0] = known[lm]
            if rm in known:
                m[2] = known[rm]
            if isinstance(m[0], int) and isinstance(m[2], int):
                val = OP[op](m[0],m[2])
                if monkey == "root":
                    return val
                unknown.pop(monkey)
                known[monkey]=val

class SolutionNotFound(Exception):
    """"""

######## Part 2 ##########
def p2(expect=301 if USING_EXAMPLE else 3330805295850):
    _known = {}
    _unknown = {}
    for line in PARSED:
        match line[0]:
            case 0, xname, xlhs, xop, xrhs:
                _unknown[xname] = [xlhs,xop,xrhs]
            case 1, xname, val:
                _known[xname] = val

    search = [0,1<<63]
    while True:
        humn = sum(search)//2
        _known["humn"] = humn
        known = _known.copy()
        unknown = deepcopy(_unknown)
        try:
            while True:
                monkeys = list(unknown.keys())
                for monkey in monkeys:
                    m = unknown[monkey]
                    lm, op, rm = m
                    if lm in known:
                        m[0] = known[lm]
                    if rm in known:
                        m[2] = known[rm]
                    if isinstance(m[0], int) and isinstance(m[2], int):
                        val = OP[op](m[0],m[2])
                        if monkey == "root":
                            if m[0] == m[2]:
                                return humn
                            step = (search[1]-search[0])//2
                            if m[0] > m[2]:
                                search[0] += step
                            else:
                                search[1] -= step
                            raise SolutionNotFound
                        unknown.pop(monkey)
                        known[monkey]=val
        except SolutionNotFound:
            pass


if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?(NS)
