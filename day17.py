# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path
import visualizations as viz
import numpy as np

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()[0]
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace(viz=True, boards=[])

# ARRAY = np.zeros((z,y,x), dtype="uint8") # 3D Array
# ARRAY_SLICE = ARRAY[0:2,0:3,22:26] # 2 layers, 3 rows, 4 columns
# ARRAY_SLICE = ARRAY[0:2,:,22:26] # 2 layers, all rows, 4 columns
# Map(ARRAY).show()

SHAPES = [
    np.array([1,1,1,1], dtype="uint8"),

    np.array([[0,2,0],
              [2,2,2],
              [0,2,0]], dtype="uint8"),

    np.array([[0,0,3],
              [0,0,3],
              [3,3,3]], dtype="uint8"),

    np.array([[6],
              [6],
              [6],
              [6]], dtype="uint8"),

    np.array([[5,5],
              [5,5]], dtype="uint8"),
]

class Shape:
    INDEX = 0
    def __init__(self):
        self.s = SHAPES[Shape.INDEX]
        try:
            self.h, self.w = self.s.shape
        except ValueError:
            self.w = self.s.shape[0]
            self.h = 1
        Shape.INDEX = (Shape.INDEX + 1) % 5

FLOOR = 50
BOARD_WIDTH = 7

class Game:
    def __init__(self,instructions):
        self.board = np.zeros((FLOOR, BOARD_WIDTH), dtype="uint8")
        self.instructions = instructions
        self.instruction_index = -1
        self.trimmed = 0

    @property
    def next_instruction(self):
        self.instruction_index = (self.instruction_index+1) % len(self.instructions)
        return self.instructions[self.instruction_index]

    def trim_lines(self):
        while self.height > FLOOR - 7:
            self.trimmed += 1
            self.board[1:FLOOR,:] = self.board[0:FLOOR-1,:]
            if NS.viz:
                NS.boards.append(self.board.copy())

    def add_new_shape(self):
        self.trim_lines()
        shape = Shape()
        shape.x = 2
        try:
            base = np.where(self.board != 0)[0][0]
        except IndexError:
            base = FLOOR
        shape.y = base - 3 - shape.h
        return shape

    def plant_shape(self):
        s = self.shape
        self.board[s.y:s.y+s.h,s.x:s.x+s.w] += s.s
        if NS.viz:
            NS.boards.append(self.board.copy())

    def shape_overlaps(self,x,y):
        s = self.shape
        return (self.board[y:y+s.h,x:x+s.w] * s.s).any()

    @property
    def height(self):
        try:
            return FLOOR - np.where(self.board != 0)[0][0]
        except IndexError:
            return 0

    def move_shape(self):
        s = self.shape
        x = s.x
        y = s.y
        if self.next_instruction == ">":
            x += 1
            if x + s.w > BOARD_WIDTH or self.shape_overlaps(x,y):
                x -= 1
        else:
            x -= 1
            if x < 0 or self.shape_overlaps(x,y):
                x += 1
        s.x = x

        y += 1
        if y + s.h > FLOOR or self.shape_overlaps(x,y):
            y -= 1
            self.plant_shape()
            return False
        else:
            s.y = y
        return True

    def drop_new_shape(self):
        self.shape = self.add_new_shape()
        while self.move_shape():
            pass

    @property
    def depth_map(self):
        m = [0]*7
        try:
            nonzero = np.where(self.board != 0)
            nzxy = zip(nonzero[0], nonzero[1])
            for y,x in nzxy:
                if not m[x]:
                    m[x] = y
                if all(m):
                    break
        except:
            pass
        m = [FLOOR-(h or FLOOR) for h in m]
        miny = min(m)
        m = [h-miny for h in m]
        return tuple(m)

    @property
    def state(self):
        return f"{max(self.depth_map)}##{self.instruction_index}#{Shape.INDEX}##{self.depth_map}"

######## Part 1 ##########
def p1(expect=3130):
    NS.viz = True
    tetris = Game(TEXT)
    for _ in range(2022):
        tetris.drop_new_shape()
    return tetris.height + tetris.trimmed

######## Part 2 ##########
def p2(expect=1556521739139):
    NS.viz = False
    Shape.INDEX = 0
    tetris = Game(TEXT)
    states = dict()
    state = None
    turn = 0
    countdown = 10

    while True:
        turn += 1
        tetris.drop_new_shape()
        state = tetris.state
        if state in states:
            break
        states[state] = turn, tetris.height + tetris.trimmed

    revlookup = {v[0]:v[1] for v in states.values()} # key by turn value is height
    base_turn, base_height = states[state]
    repeat_turn, repeat_height = turn, tetris.height + tetris.trimmed
    cycle_length = repeat_turn - base_turn
    cycle_height = repeat_height - base_height
    target = 1_000_000_000_000
    target -= base_turn
    tcycles, tsteps = divmod(target, cycle_length)
    cycle_turn = base_turn + tsteps
    cycle_turn_height = revlookup[cycle_turn]
    return tcycles * cycle_height + cycle_turn_height

if __name__ == "__main__":
    show(p1, p2)
    viz.viz17(NS)
