from utils import load, show, day, TRACE, Map, Path, NS
from PIL import Image
from matplotlib import pyplot as plt
import numpy as np
from collections import Counter

def viz1a(elves):
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

def viz1b(elves):
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

# def viz1(depths):
#     # visualize the depth map
#     div = max(depths)//100 + 1
#     viz = Map(["~"*(x//div) for x in depths])
#     viz.setcolour("~",(0,128,128))
#     viz.img = viz.img.resize((100, 100))
#     viz.img = viz.img.transpose(Image.TRANSPOSE)
#     viz.add_a_submarine(15,5)
#     viz.img.save(Path(__file__).parent / 'output' / 'day1.png')

# def viz2b(tracker):
#     # visualize the depth map
#     viz = Map([" "*100]*100)
#     viz.setcolour("#",(255,255,0))
#     for pos in tracker:
#         viz.set(pos, '#')
#     viz.add_a_submarine(99,99)
#     viz.img.save(Path(__file__).parent / 'output' / 'day2b.png')

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
