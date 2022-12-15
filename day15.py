# import our helpers
from utils import load, show, day, TRACE, Map, Path, USING_EXAMPLE

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()

# parse the input
def parse(line):
    # Sensor at x=2391367, y=3787759: closest beacon is at x=2345659, y=4354867
    field = line.split()
    x1=int(field[2].split("=")[1][:-1]) # x=2391367,
    y1=int(field[3].split("=")[1][:-1]) # y=3787759:
    x2=int(field[8].split("=")[1][:-1]) # x=2345659,
    y2=int(field[9].split("=")[1])      # y=4354867
    return (x1,y1),(x2,y2)

def dist(p1,p2):
    x1,y1=p1
    x2,y2=p2
    return (max(x1,x2)-min(x1,x2))+(max(y1,y2)-min(y1,y2))

class Sensor:
    def __init__(self, spos, bpos):
        self.pos = spos
        self.beacon = bpos
        self.dist = dist(spos,bpos)
        self.minx = spos[0] - self.dist
        self.maxx = spos[0] + self.dist

    def can_see(self, pos):
        """pos is covered by this beacon"""
        return dist(pos,self.pos) <= self.dist

    def next_unknown_x(self, pos):
        # If this beacon covers pos return the next pos.x for pos.y
        # which it doesn't so we can skip a lot of x value tests
        x,y=pos
        px,py = self.pos
        if self.can_see(pos):
            yoffset = max(y,py)-min(y,py)
            xoffset = x-px
            xdist = self.dist-yoffset-xoffset
            return x + xdist + 1 # next free x on row y
        else:
            return x # not known by this beacon

PARSED = [parse(_) for _ in TEXT]
SENSORS = [Sensor(spos,bpos) for spos,bpos in PARSED]
BEACONS = [bpos for _,bpos in PARSED]

######## Part 1 ##########
def p1(expect=4424278):
    """painful brute force"""
    tot = 0
    row = 10 if USING_EXAMPLE else 2_000_000
    minx = min([sensor.minx for sensor in SENSORS])
    maxx = max([sensor.maxx for sensor in SENSORS])
    for x in range(minx, maxx+1):
        if (x,row) not in BEACONS:
            if any(sensor.can_see((x,row)) for sensor in SENSORS):
                tot += 1
    return tot # count of visible space with no beacon

######## Part 2 ##########
def p2(expect=10382630753392):
    """smart brute force"""
    x,y = (0,0)
    cols = rows = 20 if USING_EXAMPLE else 4_000_000
    while y <= rows:
        while x <= cols:
            cmpx = x
            for sensor in SENSORS:
                x = sensor.next_unknown_x((x,y))
                if x > cols:
                    break
            if x == cmpx:
                return x * 4_000_000 + y # "tuning frequency"
        (x,y) = (0, y+1) # start again at beginning of next row
    raise RuntimeError("No solution found!")

if __name__ == "__main__":
    show(p1, p2)
