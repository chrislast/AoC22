# import our helpers
from types import SimpleNamespace
from utils import load, show, day, TRACE, Map, Path, decode4x6font, USING_EXAMPLE
import visualizations as viz

####### GLOBALS #########

# load todays input data as a docstring
TEXT = load(day(__file__)).splitlines()
# convenient for passing working between parts 1 and 2, and relevant stuff to vizualations 
NS = SimpleNamespace()

######## Part 1 ##########
def p1(expect=13140 if USING_EXAMPLE else 12980):
    t=0
    rx=1
    look=[0]*1000
    for line in TEXT:
        match line.split():
            case ["noop"]:
                t+=1
            case ["addx", v]:
                t+=2
                rx += int(v)
        look[(t+20)//40]=rx
    strength = 0
    for i,v in enumerate(range(20,t+1,40)):
        strength += look[i]*v
    return strength

######## Part 2 ##########
def p2(expect="????????" if USING_EXAMPLE else "BRJLFULP"):
    t=0
    rx=1
    screen=[["."]*40,["."]*40,["."]*40,["."]*40,["."]*40,["."]*40]

    def draw(cycle):
        """update the screen at current pixel"""
        y,x = divmod(cycle,40)
        if x in (rx-1, rx, rx+1):
            #print(y,x,screen)
            screen[y][x] = "#"

    # walk program drawing each cycle
    draw(t)
    for line in TEXT:
        match line.split():
            case ["noop"]:
                t+=1
                draw(t)
            case ["addx", v]:
                t+=1
                draw(t)
                t+=1
                rx += int(v)
                draw(t)

    # view (and decode) screen array
    s=""
    xyon = []
    for y, row in enumerate(screen):
        for x, col in enumerate(row):
            s+=col
            #showboating
            if col == "#":
                xyon.append((x,y))
        s+="\n"
    #print(s)
    NS.screen = s
    return decode4x6font(xyon)


if __name__ == "__main__":
    show(p1, p2)
    Map(NS.screen.splitlines()).resize(4).save("output/day10b.png")
