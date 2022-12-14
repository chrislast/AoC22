# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE
import visualizations as viz
import numpy as np
import re

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

np.set_printoptions(threshold=np.inf)

# Load a 2-D Map (fills missing values in text input with 0s and creates 2D array)
M=Map(TEXT[:-2])
ARRAY = np.array(M.img) # part2 uses the raw array
H,W = ARRAY.shape

# change spaces to 0 for OFFMAP
for y,x in zip(*np.where(ARRAY==ord(" "))):
    ARRAY[y,x] = 0

# add a 1-pixel border to save us checking map bounds in part 1
ARR=np.zeros((H+2,W+2),dtype="uint8")
ARR[1:H+1,1:W+1] = ARRAY[:,:]
M=Map(ARR) # and resave for part 1 use

STARTPOS = TEXT[0].index(".")+1,1
INSTRUCTIONS = TEXT[-1]

STEP={0: ( 0,-1),
     90: ( 1, 0),
    180: ( 0, 1),
    270: (-1, 0)}

WALL=ord("#")
OPEN=ord(".")
PATH=ord("~")
ORIGIN=ord("@")
DESTINATION=ord("X")
OFFMAP = 0

######## Part 1 ##########
def forward(pos, direction):
    px,py = pos
    x,y = STEP[direction]
    npos = (px+x,py+y)
    if M.get(npos) != OFFMAP:
        return npos
    npos = pos
    while M.get(npos) != OFFMAP:
        npos = (npos[0]-x,npos[1]-y)
    return (npos[0]+x,npos[1]+y)

def newpos(pos, direction, steps):
    for _ in range(steps):
        npos = forward(pos, direction)
        found = M.get(npos)
        if found == WALL:
            return pos
        else:
            M.set(npos, PATH)
            pos = npos
    return pos

def p1(expect=6032 if USING_EXAMPLE else 103224):
    M.set(STARTPOS, PATH)
    x,y = STARTPOS
    instructions = INSTRUCTIONS
    dirn = 90
    idx = 0
    while idx<len(instructions):
        if instructions[idx] == "L":
            dirn = (dirn + 270) % 360
            idx += 1
        elif instructions[idx] == "R":
            dirn = (dirn + 90) % 360
            idx += 1
        else:
            i = re.match(r"(?P<dist>[0-9]*).*", instructions[idx:])
            steps = i.groupdict()["dist"]
            x,y = newpos((x,y), dirn, int(steps))
            idx += len(steps)
    ddv = ((dirn+270)//90)%4
    NS.p1 = M
    return 1000*y + 4*x + ddv

######## Part 2 ##########

class CubeMap:
    def __init__(self):
        # allow a border around map for edge reached
        self.dim3d = 6 if USING_EXAMPLE else 52
        self.rotations = []
        self.from_2d()
        self.x = self.y = 1 # all the action happens on z=0 plane
        self.set(ORIGIN)
        self.path = [] # only used to determine final facing

    def rotate_forward(self):
        self.rotations.append("rf")
        self.cube = np.rot90(self.cube,k=1,axes=(0,1))

    def rotate_backward(self):
        self.rotations.append("rb")
        self.cube = np.rot90(self.cube,k=1,axes=(1,0))

    def rotate_right(self):
        self.rotations.append("rr")
        self.cube = np.rot90(self.cube,k=1,axes=(2,0))

    def rotate_left(self):
        self.rotations.append("rl")
        self.cube = np.rot90(self.cube,k=1,axes=(0,2))

    def turn_left(self):
        self.rotations.append("tl")
        saved = self.get()
        self.set(DESTINATION)
        self.cube = np.rot90(self.cube,k=1,axes=(2,1))
        x,y = np.where(self.cube[0]==DESTINATION)
        self.y, self.x = x[0], y[0]
        self.set(saved)

    def turn_right(self):
        self.rotations.append("tr")
        saved = self.get()
        self.set(DESTINATION)
        self.cube = np.rot90(self.cube,k=1,axes=(1,2))
        x,y = np.where(self.cube[0]==DESTINATION)
        self.y, self.x = x[0], y[0]
        self.set(saved)

    def set(self, val):
        self.cube[0,self.y,self.x] = val

    def get(self):
        return self.cube[0,self.y,self.x]

    def to_2d(self):
        # save cube state
        cube = self.cube.copy()
        x, y = self.x, self.y
        rotations = self.rotations.copy()

        for inst in self.rotations[::-1]:
            match inst:
                case "rr": self.rotate_left()
                case "rl": self.rotate_right()
                case "rf": self.rotate_backward()
                case "rb": self.rotate_forward()
                case "tr": self.turn_left()
                case "tl": self.turn_right()
                case x: raise ValueError(x)

        face2d = lambda: self.cube[0,1:-1,1:-1]
        if USING_EXAMPLE:
            map2d = np.zeros((12,16),dtype="uint8")
            map2d[0:4, 8:12] = face2d()
            self.rotate_forward()
            map2d[4:8, 8:12] = face2d()
            self.rotate_right()
            map2d[4:8, 4:8 ] = face2d()
            self.rotate_right()
            map2d[4:8, 0:4 ] = face2d()
            self.rotate_left()
            self.rotate_left()
            self.rotate_forward()
            map2d[8:12, 8:12] = face2d()
            self.rotate_left()
            map2d[8:12, 12:16] = face2d()
        else:
            map2d = np.zeros((200,150),dtype="uint8")
            map2d[0:50,50:100] = face2d()
            self.rotate_left()
            map2d[0:50,100:150] = face2d()
            self.rotate_right()
            self.rotate_forward()
            map2d[50:100,50:100] = face2d()
            self.rotate_forward()
            map2d[100:150,50:100] = face2d()
            self.rotate_right()
            map2d[100:150,0:50] = face2d()
            self.rotate_forward()
            map2d[150:200,0:50] = face2d()

        self.cube = cube # restore original state
        self.rotations = rotations
        self.x, self.y = x, y
        return map2d

    def from_2d(self):
        if USING_EXAMPLE:
            self.cube = np.zeros((6,6,6),dtype="uint8")
            self.cube[0,1:-1,1:-1] = ARRAY[0:4, 8:12]
            self.rotate_forward()
            self.cube[0,1:-1,1:-1] = ARRAY[4:8, 8:12]
            self.rotate_right()
            self.cube[0,1:-1,1:-1] = ARRAY[4:8, 4:8 ]
            self.rotate_right()
            self.cube[0,1:-1,1:-1] = ARRAY[4:8, 0:4 ]
            self.rotate_left()
            self.rotate_left()
            self.rotate_forward()
            self.cube[0,1:-1,1:-1] = ARRAY[8:12, 8:12]
            self.rotate_left()
            self.cube[0,1:-1,1:-1] = ARRAY[8:12, 12:16]
            self.rotate_right()
            self.rotate_forward()
            self.rotate_forward()
        else:
            self.cube = np.zeros((52,52,52),dtype="uint8")
            self.cube[0,1:-1,1:-1] = ARRAY[0:50,50:100]
            self.rotate_left()
            self.cube[0,1:-1,1:-1] = ARRAY[0:50,100:150]
            self.rotate_right()
            self.rotate_forward()
            self.cube[0,1:-1,1:-1] = ARRAY[50:100,50:100]
            self.rotate_forward()
            self.cube[0,1:-1,1:-1] = ARRAY[100:150,50:100]
            self.rotate_right()
            self.cube[0,1:-1,1:-1] = ARRAY[100:150,0:50]
            self.rotate_forward()
            self.cube[0,1:-1,1:-1] = ARRAY[150:200,0:50]
            self.rotate_backward()
            self.rotate_left()
            self.rotate_forward()
            self.rotate_forward()

    def go_forward(self, steps):
        for _ in range(steps):
            y = self.y
            # go forward
            y -= 1

            if self.cube[0,y,self.x] == WALL:
                y += 1
                break

            # if we are on rotate edge
            if y == 0:
                # rotate
                self.rotate_backward()
                # and step onto new cube face
                y = 4 if USING_EXAMPLE else 50
                # if we arrived at a wall
                if self.cube[0, y, self.x] == WALL:
                    # go back and stop
                    self.rotate_forward()
                    y = 1
                    break

            self.y = y
            self.path.append((self.x, self.y))
            self.set(PATH)


def p2(expect=5031 if USING_EXAMPLE else 189097):
    cube = CubeMap()
    instructions = INSTRUCTIONS
    idx = 0
    dbg = lambda: Map(cube.to_2d()).show()
    cube.turn_right()
    while idx<len(instructions):
        if instructions[idx] == "L":
            cube.turn_left() # move the world not santa!
            idx += 1
        elif instructions[idx] == "R":
            cube.turn_right() # move the world not santa!
            idx += 1
        else:
            i = re.match(r"(?P<dist>[0-9]*).*", instructions[idx:])
            steps = i.groupdict()["dist"]
            cube.go_forward(int(steps))
            idx += len(steps)
    cube.set(DESTINATION)
    map2d = cube.to_2d()
    res = np.where(map2d==DESTINATION)
    y,x = list(zip(*res))[0]
    # Map(map2d).show()
    NS.p2 = map2d
    # @@ I visually inspected the 2d map at this point to work out the possible facings, there were two, then tried both!
    facing = 3 if USING_EXAMPLE else 1
    return 1000*(y+1) + 4*(x+1) + facing


if __name__ == "__main__":
    show(p1, p2)
    NS.p1.img.resize((456,606)).save("output/day22a.png")
    Map(NS.p2).img.resize((450,600)).save("output/day22b.png")
