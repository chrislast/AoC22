from utils import load, show, day, TRACE, Map, Path, NS
from PIL import Image, ImageDraw, ImageFont
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

def viz1p1(elves):
    """bar graph"""
    fig, ax = plt.subplots()
    mx = max(elves)
    for idx, elf in enumerate(elves):
        if elf == mx:
            ax.bar(idx, elf, width=1.0, color="gold")
        else:
            ax.bar(idx, elf, width=1.0, color="silver")
    ax.set(title="max(elf)")
    ax.grid(visible=True, axis="y")
    ax.set_xlim(0,len(elves)-1)
    ax.set_xlabel("elf")
    ax.set_ylabel("total calories")
    fig.set_tight_layout(True)
    fig.savefig(Path(__file__).parent / 'output' / 'day1a.png')

def viz1p2(elves):
    """bar graph"""
    fig, ax = plt.subplots()
    elves = sorted(elves)
    for idx, elf in enumerate(elves[:-3]):
    	ax.bar(idx, elf, width=1.0, color="silver")
    for idx2, elf in enumerate(elves[-3:]):
        ax.bar(idx+idx2, elf, width=1.0, color="gold")            
    ax.set(title="sorted(elves)[-3:]")
    ax.grid(visible=True, axis="y")
    ax.set_xlim(0,len(elves)-1)
    ax.set_xlabel("elf")
    ax.set_ylabel("total calories")
    fig.set_tight_layout(True)
    fig.savefig(Path(__file__).parent / 'output' / 'day1b.png')


class RockPaperScissorsGIF:
    def __init__(self):
        self.gif = []
        self.round = 0
        self.font = ImageFont.load_default()
        rps = Image.open("resources/rps.png").resize((120,100)).convert("RGB")
        self.rps = {
            "R": rps.crop((60,10,120,60)).transpose(Image.Transpose.FLIP_LEFT_RIGHT),
            "P": rps.crop((20,50,80,100)),
            "S": rps.crop((0,0,60,50)),
        }

    def play(self, game):
        for rnd, tot in game:
                self.play_round(*rnd.split(), tot)

    def play_round(self, rps1, rps2, score):
        self.round += 1
        img = Image.new("RGB", (120,80)) # width, height
        #img.putpalette(palette)
        # show round
        d = ImageDraw.Draw(img)
        d.text((5,5), f"[{self.round:4d}] score:{score:5d}", fill=(255,255,255), font=self.font)
        # show player 1
        img.paste(self.rps[rps1], (0,30))
        # show player 2
        img.paste(self.rps[rps2].transpose(Image.Transpose.FLIP_LEFT_RIGHT),(60,30))
        # show score
        self.gif.append(img)

    def write(self, fname):
        self.gif[0].save(fname, append_images=self.gif[1:], save_all=True) #, palette=self.palette)

def viz2p1(game):
    rps = RockPaperScissorsGIF()
    rps.play(game)
    rps.write("output/day2a.gif")

def viz2p2(game):
    rps = RockPaperScissorsGIF()
    rps.play(game)
    rps.write("output/day2b.gif")

# def viz1(depths):
#     # visualize the depth map
#     div = max(depths)//100 + 1
#     viz = Map(["~"*(x//div) for x in depths])
#     viz.setcolour("~",(0,128,128))
#     viz.img = viz.img.resize((100, 100))
#     viz.img = viz.img.transpose(Image.TRANSPOSE)
#     viz.add_a_submarine(15,5)
#     viz.img.save(Path(__file__).parent / 'output' / 'day1.png')

def viz4p1(elfduties):
    # visualize the depth map
    viz = Map(["0"*100]*len(elfduties))
    viz.setcolour("0",(0,0,0))
    viz.setcolour("1",(255,0,0))
    viz.setcolour("2",(0,255,255))
    viz.setcolour("3",(255,255,255))
    for y, elves in enumerate(elfduties):
        e1, e2 = elves
        for x in e1:
            viz.set((x,y),"1")
        for x in e2:
            viz.set((x,y),viz.get((x,y))+2)
    i2 = viz.img.resize((200,200))
    i2.save(Path(__file__).parent / 'output' / 'day4ax.png')
    viz.img.resize((100,len(elfduties)*4)).save(Path(__file__).parent / 'output' / 'day4a.png')


def viz8p2(ns, m):
    w,h = m.img.size
    for _ in "0123456789":
        m.setcolour(_,(20,50+15*int(_),20))
    m.set(ns.treehouse,1)
    m.img.resize((w*4,h*4)).save("output/day8b.png")

def viz8p1(ns, m):
    w,h = m.img.size
    for x in range(w):
        for y in range(h):
            if (x,y) not in ns.visible:
                m.set((x,y),0)
    m.img.resize((w*4,h*4)).save("output/day8a.png")

def viz9(fname, ropes):
    BLACK = 0
    START = 1
    KNOT = 2
    TAIL = 3
    PALETTE = (0,0,0,  0,0,255,  128,128,128,  200,0,0)

    xmin = ymin = xmax = ymax = 0
    # find the corners
    for rope in ropes:
        for x,y in rope:
            xmin = min(x, xmin)
            ymin = min(y, ymin)
            xmax = max(x, xmax)
            ymax = max(y, ymax)

    xmin -= 1; ymin -= 1; xmax += 1; ymax += 1
    dx = -xmin; dy = -ymin

    h=ymax-ymin+1
    w=xmax-xmin+1

    gif = []
    been = set()
    for rope in ropes:
        img = Image.new("P", (w,h))
        img.putpalette(PALETTE)
        gif.append(img)
        for x,y in been:
            img.putpixel((x+dx, y+dy), TAIL)
        img.putpixel((0+dx, 0+dy), START)
        for x,y in rope:
            img.putpixel((x+dx, y+dy), KNOT)
        been.add((x, y))
    img.save(fname, append_images=gif, save_all=True)

def viz9p1(ropes):
    viz9("output/day9a.gif", ropes)

def viz9p2(ropes):
    viz9("output/day9b.gif", ropes)


def viz12p1(ns):
    # update map palette
    for _ in "abcdefghijklmnopqrstuvwxyz":
        o = ord(_) - ord("a")
        ns.map.setcolour(_,(o*10, 128+o*5, o*10))
    ns.map.setcolour("S", (255,0,0))
    ns.map.setcolour("P", (255,0,255))
    ns.map.setcolour("E", (0,0,255))

    pth = ns.p1
    img = ns.map.img.copy()
    img.putpixel(pth[0], ord("S"))
    img.putpixel(pth[-1], ord("E"))
    w,h = img.size
    img = img.resize((w*3, h*3))
    for _ in pth:
        x,y=_
        img.putpixel((x*3+1, y*3+1), ord("P"))
    img.resize((w*9, h*9)).save("output/day12a.png")

def viz12p2(ns):
    pth = ns.p2
    # all elevation a are target in part 2
    ns.map.setcolour("a", (0,0,255))
    img = ns.map.img.copy()
    img.putpixel(pth[0], ord("S"))
    w,h = img.size
    img = img.resize((w*3, h*3))
    for _ in pth:
        x,y=_
        img.putpixel((x*3+1, y*3+1), ord("P"))
    img.resize((w*9, h*9)).save("output/day12b.png")

def viz14(ns):
    array, floor, minx, maxx = ns.p1
    array[0,500] = 1
    m=Map(array[:floor+2,minx-1:maxx+2])
    w,h = m.img.size
    m.img.resize((w*3,h*3)).save("output/day14a.png")
    array, floor, minx, maxx = ns.p2
    array[0,500] = 1
    m=Map(array[:floor+2,minx-1:maxx+2])
    w,h = m.img.size
    m.img.resize((w*3,h*3)).save("output/day14b.png")

def viz17(ns):
    gif = []
    font = ImageFont.load_default()
    for h, board in ns.boards:
        img = Map(board).img.resize((7*5,50*5))
        d = ImageDraw.Draw(img)
        d.text((1,1), f" {h:4d} ", fill=(200,200,200), font=font)
        gif.append(img)
    gif[-1].save("output/day17a.gif", append_images=gif, save_all=True)

# def viz3a(counters):
#     """stacked bar graph"""
#     fig, ax = plt.subplots()
#     xlabels = range(len(counters))
#     ones = [_['1'] for _ in counters]
#     noughts = [_['0'] for _ in counters]
#     ax.bar(xlabels, noughts, label="0")
#     ax.bar(xlabels, ones, label="1", bottom=noughts)
#     ax.set(ylim=[450, 550], title="Bit Value Counters")
#     ax.grid(visible=True, axis="y")
#     ax.set_xlabel("bit position")
#     ax.set_xticks(range(0,12))
#     ax.set_yticks(range(450,560,10))
#     ax.legend()
#     fig.set_tight_layout(True)
#     fig.savefig(Path(__file__).parent / 'output' / 'day3a.png')

# def viz3b(counters):
#     """3d stacked bar graph"""
#     # setup the figure and axes
#     fig = plt.figure(figsize=(7,6))
#     ax = fig.add_subplot(111, projection='3d', title="Valid codes remaining")
#     width = 0.75
#     depth = 0.5
#     x = [0,1,2,3,4,5,6,7,8,9,10,11]*2
#     y = [0]*12 + [1]*12
#     z = [0]*24
#     ones = [c['1'] for c in counters]
#     noughts = [c['0'] for c in counters]
#     ax.set_xticks(range(0,12))
#     ax.set_xlabel("bits checked")
#     ax.set_ylabel("oxygen            CO2")
#     ax.set_yticks([])
#     ax.bar3d(x, y, z, width, depth, noughts, shade=True, label="0")
#     ax.bar3d(x, y, noughts, width, depth, ones, shade=True, label="1")
#     fig.set_tight_layout(True)
#     fig.savefig(Path(__file__).parent / 'output' / 'day3b.png')

# def viz5a(sea):
#     sea.save(Path(__file__).parent / 'output' / 'day5a.png')

# def viz5b(sea):
#     sea.save(Path(__file__).parent / 'output' / 'day5b.png')

# def viz6a(lanternfish):
#     """stacked bar graph"""
#     data = Counter(lanternfish)
#     fig, ax = plt.subplots()
#     xlabels = []
#     fish = []
#     for days in range(9):
#         xlabels.append(days)
#         fish.append(data.get(days, 0))
#     ax.bar(xlabels, fish, label="day 80 population")
#     ax.grid(visible=True, axis="y")
#     ax.set_xlabel("days to next birth")
#     ax.set_xticks(range(9))
#     ax.legend()
#     fig.set_tight_layout(True)
#     fig.savefig(Path(__file__).parent / 'output' / 'day6a.png')

# def viz6b(population):
#     """stacked bar graph"""
#     data = population[-1]
#     fig, ax = plt.subplots()
#     xlabels = []
#     fish = []
#     for days in range(9):
#         xlabels.append(days)
#         fish.append(data.get(days, 0))
#     ax.bar(xlabels, fish, label="day 256 population")
#     ax.grid(visible=True, axis="y")
#     ax.set_xlabel("days to next birth")
#     ax.set_xticks(range(9))
#     ax.legend()
#     fig.set_tight_layout(True)
#     fig.savefig(Path(__file__).parent / 'output' / 'day6b.png')

# def viz7b(scatter):
#     fig, ax = plt.subplots()
#     xdata = [_[0] for _ in scatter]
#     ydata = [_[1] for _ in scatter]
#     ax.plot(xdata, ydata)
#     ax.set_xlabel("crab submarine position")
#     ax.set_ylabel("fuel used")
#     fig.set_tight_layout(True)
#     fig.savefig(Path(__file__).parent / 'output' / 'day7b.png')

# def viz9a(func, seafloor):
#     for val in "0123456789":
#         # make the color map brown
#         sat = (int(val)+3)/10
#         seafloor.setcolour(val, (int(0xa5*sat), int(0x2a*sat), int(0x2a*sat)))
#     func(viz=True)
#     seafloor.img.resize((100,100)).save(Path(__file__).parent / 'output' / 'day9athumb.png')
#     seafloor.save(Path(__file__).parent / 'output' / 'day9a.png')
#     w, h = seafloor.img.size
#     x = np.array([x for y in range(h) for x in range(w)]).reshape(w,h)
#     y = np.array([y for y in range(h) for x in range(w)]).reshape(w,h)
#     z = np.array([_-48 for _ in seafloor.img.getdata()]).reshape(w,h)
#     fig, ax = plt.subplots(subplot_kw=dict(projection='3d'))
#     ax.plot_surface(x, y, z)
#     ax.set_axis_off()
#     ax.set(zlim=[-100, 100])
#     fig.set_tight_layout(True)
#     full = Path(__file__).parent / 'output' / 'day9a2.png'
#     fig.savefig(full, dpi=200)
#     img = Image.open(full)
#     cropped = img.crop((290,280,1000,650))
#     cropped.save(Path(__file__).parent / 'output' / 'day9a2.png')

# def viz9b(func, seafloor):
#     seafloor.setcolour(255, (0, 255, 255))
#     func(viz=True)
#     seafloor.savegif(Path(__file__).parent / 'output' / 'day9b.gif', duration=5)

# def viz11(func, cave, outfile):
#     for _ in range(1,10):
#         cave.setcolour(_,(_*12,_*12,_*12))
#     cave.setcolour(0,(255,255,255))
#     func(viz=True)
#     cave.savegif(outfile)

# def viz13a(dots):
#     # pad image 40*6 image to make it readable
#     xl=[x for x,y in dots]
#     yl=[y for x,y in dots]
#     arr=np.zeros((max(yl)+1,max(xl)+1), dtype=int)
#     for dot in dots:
#         arr[dot[::-1]] = 1
#     m=Map(arr)
#     m.save(Path(__file__).parent / 'output' / 'day13a.png')

# def viz13b(dots):
#     # pad image 40*6 image to make it readable
#     m=Map([[0]*42]*8)
#     for dot in dots:
#         # offset dot position to keep 1 pixel margin
#         m.set((dot[0]+1,dot[1]+1),1)
#     m.save(Path(__file__).parent / 'output' / 'day13b.png')

# def viz15a(route):
#     m=Map(np.zeros((100,100), dtype=int))
#     m.set((0,0), 255)
#     m.setcolour(255,(255,255,255))
#     for pos in route:
#         m.set(pos, 255)
#     m.save(Path(__file__).parent / 'output' / 'day15a.png')

# def viz15b(route):
#     m=Map(np.zeros((500,500), dtype=int))
#     m.set((0,0), 255)
#     m.setcolour(255,(255,255,255))
#     for pos in route:
#         m.set(pos, 255)
#     m.save(Path(__file__).parent / 'output' / 'day15b.png')

# def viz20a(maps):
#     gifmap = maps[0]
#     for m in maps[1::2]:
#         gifmap.img.putdata(m.img.getdata())
#         gifmap.addtogif()
#     gifmap.savegif(Path(__file__).parent / 'output' / 'day20a.gif')

# def viz20b(maps):
#     gifmap = maps[0]
#     for m in maps[1::2]:
#         gifmap.img.putdata(m.img.getdata())
#         gifmap.addtogif()
#     gifmap.savegif(Path(__file__).parent / 'output' / 'day20b.gif')
