# AoC22
[Advent of Code 2022](https://adventofcode.com/2022) Python 3.11 solutions

## Diary

|&nbsp;|Challenge | Execution Time | Visualisation | Notes
|------|--------- | -------------- | ------------- | -----
|1a|Calorie Counting<br />[🌐](https://adventofcode.com/2022/day/1)[💾](./day1.py) | 0ms | [![](./output/day1a.png)](./output/day1a.png) | Find the elf with the most calorific food <br />__4 minutes__
|1b|&nbsp; | 0ms | [![](./output/day1b.png)](./output/day1b.png)  | Find the 3 elves with the most calorific food<br /><br />**04:49** elapsed time was good enough for rank **#1191** a mere 1091 ranks outside the points leaderboard so I'll sleep in tomorrow! <br />__<1 minute__
|2a|Rock Paper Scissors<br />[🌐](https://adventofcode.com/2022/day/2)[💾](./day2.py) | 1ms | [![](./output/day2a.gif)](./output/day2a.gif) play! | XYZ = rock paper scissors <br />__21 minutes__
|2b|&nbsp; | 1ms | [![](./output/day2b.gif)](./output/day2b.gif)  play!| XYZ = lose draw win <br />__4 minutes__
|3a|Rucksack Reorganization<br />[🌐](https://adventofcode.com/2022/day/3)[💾](./day3.py) | 0ms | [![](./output/day3a.png)](./output/day3a.png) | find the set intersection <br />__19 minutes__
|3b|&nbsp; |1ms | [![](./output/day3b.png)](./output/day3b.png)  | intersections pt 2 <br />__20 minutes__
|4a|Camp Cleanup<br />[🌐](https://adventofcode.com/2022/day/4)[💾](./day4.py) | 3ms | [![](./output/day4ax.png)](./output/day4a.png) <br />elf 1 is red<br />elf 2 is cyan<br />overlaps are white | find the subsets <br />__7 minutes__
|4b|&nbsp; | 3ms | [![](./output/day4b.png)](./output/day4b.png)  | and back to intersections <br />__2 minutes__
|5a|Supply Stacks<br />[🌐](https://adventofcode.com/2022/day/5)[💾](./day5.py) | 0ms | [![](./output/day5a.png)](./output/day5a.png) | text parsing multiple info sources and array manipulation <br />__36 minutes__
|5b|&nbsp; | 0ms | [![](./output/day5b.png)](./output/day5b.png)  | tiny change to element ordering <br />__1 minute__
|6a|Tuning Trouble<br />[🌐](https://adventofcode.com/2022/day/6)[💾](./day6.py) | 0ms | [![](./output/day6a.png)](./output/day6a.png) | Walk a long string for first occurrence of n unique characters where n=4 <br />__12 minutes__
|6b|&nbsp; | 1ms | [![](./output/day6b.png)](./output/day6b.png)  | where n=14 <br />__<1 minute__
|7a|No Space Left On Device<br />[🌐](https://adventofcode.com/2022/day/7)[💾](./day7.py) | 0ms | [![](./output/day7a.png)](./output/day7a.png) | Track folder sizes in a Linux-like file system <br />__49 minutes__
|7b|&nbsp; | 0ms | [![](./output/day7b.png)](./output/day7b.png)  | Delete the right one to start the upgrade.  Will we see more of this Linux virtual computer later? <br />__12 minutes__
|8a|Treetop Tree House<br />[🌐](https://adventofcode.com/2022/day/8)[💾](./day8.py) | 17ms | [![](./output/day8a.png)](./output/day8a.png) visible trees | find the local maximum from edges of a 2D array <br />__13 minutes__
|8b|&nbsp; | 59ms | [![](./output/day8b.png)](./output/day8b.png) tree house (white) | find the local maximums from each point in a 2D array - O(N2) alert! <br />__29 minutes__
|9a|Rope Bridge<br />[🌐](https://adventofcode.com/2022/day/9)[💾](./day9.py) | 7ms | [![](./output/day9a.gif)](./output/day9a.gif) | overslept :( then massively overcomplicated the rope tail updater by using compound if-then-elses; replaced my original 2-knot head tail solution with generic version from part 2 with length 2 <br />__40? minutes__
|9b|&nbsp; | 32ms | [![](./output/day9b.gif)](./output/day9b.gif)  | stuck for ages debugging complicated tail updater; eventually replaced that with much simpler version and it worked then simplified everything else to end up looking quite pleasing, good for animation too! <br />__96?? minutes__
|10a|Cathode-Ray Tube<br />[🌐](https://adventofcode.com/2022/day/10)[💾](./day10.py) | 0ms | [![](./output/day10a.png)](./output/day10a.png) | a comprehension test in two parts with a suitably satisfying end and an opportunity to use the new case statement<br />__21 minutes__
|10b|&nbsp;| 0ms | [![](./output/day10b.png)](./output/day10b.png)  | hmm my code is all #s... a useful reminder that [["."]\*40]\*6 gives you 6 references to the same array! <br />__35 minutes__
|11a|Monkey in the Middle<br />[🌐](https://adventofcode.com/2022/day/11)[💾](./day11.py) | 1ms | [![](./output/day11a.png)](./output/day11a.png) | easy enough to understand, slightly painful to parse, made easier especially in part 2 by monkeypatching my monkeys after creating them. Monkey business indeed! <br />__63 minutes__
|11b|&nbsp;| 196ms | [![](./output/day11b.png)](./output/day11b.png)  | I tried it without the mentioned worry reduction strategy first of course as python can handle arbitrarily big integers, but it also takes an arbitrarily very long time, so strategies it is, thankfully the required strategy didn't involve caching monkey states and came to me quite quickly, no-one wants to watch this animation! <br />__16 minutes__
|12a|Hill Climbing Algorithm<br />[🌐](https://adventofcode.com/2022/day/12)[💾](./day12.py) | 22ms | [![](./output/day12a.png)](./output/day12a.png) red=start, blue=target | The first breadth-first search problem with a twist in adjacent cell selection, find your way from the start to the top of the hill.  <br />__59 minutes__
|12b|&nbsp;| 17ms | [![](./output/day12b.png)](./output/day12b.png) red=start, blue=target| this time find your way to ground level from the top, should have been trivial swapping start position and end condition but triggered a bug in my previous solution when path hit row 0 and confused me for a long while. <br />__46 minutes__
|13a|Distress Signal<br />[🌐](https://adventofcode.com/2022/day/13)[💾](./day13.py) | 10ms | [![](./output/day13a.png)](./output/day13a.png) | fell into a bear trap; this looked like a simple flatten and native list compare problem so I thought my super small recursive flatten function would get my silver star, but the list exhaustion requirement meant I went back to the drawing board, threw out the flatten function (sent to utils.py) and hand-crafted a recursive list walker complete with print instrumentation to match the example commentary <br />__74 minutes__
|13b|&nbsp; | 21ms | [![](./output/day13b.png)](./output/day13b.png) | A lot easier than part 2 - python just needs a **\_\_lt\_\_** function in a class to sort objects so I created a very simple signal class and used the compare function from part 1 to **sorted()** all the signals, two indexes later and I was done  <br />__12 minutes__
|14a|Regolith Reservoir<br />[🌐](https://adventofcode.com/2022/day/14)[💾](./day14.py) | 255ms | [![](./output/day14a.png)](./output/day14a.png) | Thankfully I did some numpy refresher homework yesterday. the hardest part for me was probably building the map to start with<br />__49 minutes__
|14b|&nbsp;                                                                                 | 7.446s | [![](./output/day14b.png)](./output/day14b.png)  | Got some low results for sand on part2 then realised array[:,:] doesn't make a copy it's just a slice of the original so my part 2 was only showing new sand on top of the complete part 1.  changed the answer to cound sand in final array instead of tracking sand poured in (and used array.copy() too!)<br />__24 minutes__
|15a|<br />[🌐](https://adventofcode.com/2022/day/15)[💾](./day15.py) | <!-- 0.0s --> | [![](./output/day15a.png)](./output/day15a.png) | <br />
|15b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day15b.png)](./output/day15b.png)  | <br />
|16a|<br />[🌐](https://adventofcode.com/2022/day/16)[💾](./day16.py) | <!-- 0.0s --> | [![](./output/day16a.png)](./output/day16a.png) | <br />
|16b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day16b.png)](./output/day16b.png)  | <br />
|17a|<br />[🌐](https://adventofcode.com/2022/day/17)[💾](./day17.py) | <!-- 0.0s --> | [![](./output/day17a.png)](./output/day17a.png) | <br />
|17b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day17b.png)](./output/day17b.png)  | <br />
|18a|<br />[🌐](https://adventofcode.com/2022/day/18)[💾](./day18.py) | <!-- 0.0s --> | [![](./output/day18a.png)](./output/day18a.png) | <br />
|18b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day18b.png)](./output/day18b.png)  | <br />
|19a|<br />[🌐](https://adventofcode.com/2022/day/19)[💾](./day19.py) | <!-- 0.0s --> | [![](./output/day19a.png)](./output/day19a.png) | <br />
|19b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day19b.png)](./output/day19b.png)  | <br />
|20a|<br />[🌐](https://adventofcode.com/2022/day/20)[💾](./day20.py) | <!-- 0.0s --> | [![](./output/day20a.png)](./output/day20a.png) | <br />
|20b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day20b.png)](./output/day20b.png)  | <br />
|21a|<br />[🌐](https://adventofcode.com/2022/day/21)[💾](./day21.py) | <!-- 0.0s --> | [![](./output/day21a.png)](./output/day21a.png) | <br />
|21b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day21b.png)](./output/day21b.png)  | <br />
|22a|<br />[🌐](https://adventofcode.com/2022/day/22)[💾](./day22.py) | <!-- 0.0s --> | [![](./output/day22a.png)](./output/day22a.png) | <br />
|22b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day22b.png)](./output/day22b.png)  | <br />
|23a|<br />[🌐](https://adventofcode.com/2022/day/23)[💾](./day23.py) | <!-- 0.0s --> | [![](./output/day23a.png)](./output/day23a.png) | <br />
|23b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day23b.png)](./output/day23b.png)  | <br />
|24a|<br />[🌐](https://adventofcode.com/2022/day/24)[💾](./day24.py) | <!-- 0.0s --> | [![](./output/day24a.png)](./output/day24a.png) | <br />
|24b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day24b.png)](./output/day24b.png)  | <br />
|25a|<br />[🌐](https://adventofcode.com/2022/day/25)[💾](./day25.py) | <!-- 0.0s --> | [![](./output/day25a.png)](./output/day25a.png) | <br />

## Powershell

This year I am using a [powershell script](./input/download.ps1) to fetch my inputs, and open todays AoC22 puzzle triggered at 05:00:01 every morning (UK time) 🥱😴 or as soon as I log in 😊
