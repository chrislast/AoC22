# import our helpers
import sys
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
from collections import deque
####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

if len(sys.argv) > 1:
 TEXT = """
$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k
""".splitlines()[1:]

LOOKUP = {}

def sz(dct, name, curpth):
    """
    recursively walk the root directory caching directory sizes
    """
    newpth = "/".join([curpth,name])
    LOOKUP[newpth] = 0
    for k,v in dct.items():
        if isinstance(v,dict):
            sz(v,k,newpth)
            LOOKUP[newpth] += LOOKUP['/'.join([newpth,k])]
        else:
            LOOKUP[newpth] += v

######## Part 1 ##########
def p1(expect=1611443):
    root = {}
    cwd = root
    up = []

    # parse input
    for line in TEXT:
        _ = line.split()
        if _[0] == "$":
            if _[1] == "cd":
                if _[2]=="..":
                    cwd = up.pop()
                elif _[2]=="/":
                    cwd = root
                    up = []
                else:
                    up.append(cwd)
                    cwd = cwd[_[2]]

        elif _[0] == "dir":
            try:
                cwd[_[1]]
            except:
                cwd[_[1]] = {}

        else:
            cwd[_[1]]=int(_[0])

    # recursively walk the root directory caching directory sizes
    sz(root,"root", "")

    dirsizes = [v for k,v in LOOKUP.items()if v <= 100000]
    return sum(dirsizes)

######## Part 2 ##########
def p2(expect=2086088):
    capacity = 70_000_000
    needed = 30_000_000
    used = LOOKUP["/root"]
    free = capacity - used
    need_to_delete = needed - free
    dirsizes = [v for k,v in LOOKUP.items()]
    candidates = [_ for _ in dirsizes if _ >= need_to_delete]
    return min(candidates)

if __name__ == "__main__":
    show(p1, p2)
    #viz.viz?p1(NS)
    #viz.viz?p2(NS)
