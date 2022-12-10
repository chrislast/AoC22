# AoC22
[Advent of Code 2022](https://adventofcode.com/2022) Python 3 solutions

## Diary

|&nbsp;|Challenge | Execution Time | Visualisation | Notes
|------|--------- | -------------- | ------------- | -----
|1a|Calorie Counting [🌐](https://adventofcode.com/2022/day/1)[💾](./day1.py) | 0ms | [![](./output/day1a.png)](./output/day1a.png) | Find the elf with the most calorific food
|1b|&nbsp; | 0ms | [![](./output/day1b.png)](./output/day1b.png)  | Find the 3 elves with the most calorific food<br /><br />**04:49** elapsed time was good enough for rank **#1191** a mere 1091 ranks outside the points leaderboard so I'll sleep in tomorrow!
|2a|Rock Paper Scissors [🌐](https://adventofcode.com/2022/day/2)[💾](./day2.py) | 1ms | [![](./output/day2a.gif)](./output/day2a.gif) play! | XYZ = rock paper scissors
|2b|&nbsp; | 1ms | [![](./output/day2b.gif)](./output/day2b.gif)  play!| XYZ = lose draw win
|3a|Rucksack Reorganization [🌐](https://adventofcode.com/2022/day/3)[💾](./day3.py) | 0ms | [![](./output/day3a.png)](./output/day3a.png) | find the set intersection
|3b|&nbsp; |1ms | [![](./output/day3b.png)](./output/day3b.png)  | intersections pt 2
|4a|Camp Cleanup [🌐](https://adventofcode.com/2022/day/4)[💾](./day4.py) | 3ms | [![](./output/day4ax.png)](./output/day4a.png) </br />elf 1 is red</br />elf 2 is cyan</br />overlaps are white | find the subsets
|4b|&nbsp; | 3ms | [![](./output/day4b.png)](./output/day4b.png)  | and back to intersections
|5a|Supply Stacks [🌐](https://adventofcode.com/2022/day/5)[💾](./day5.py) | 0ms | [![](./output/day5a.png)](./output/day5a.png) | text parsing multiple info sources and array manipulation
|5b|&nbsp; | 0ms | [![](./output/day5b.png)](./output/day5b.png)  | tiny change to element ordering
|6a|Tuning Trouble [🌐](https://adventofcode.com/2022/day/6)[💾](./day6.py) | 0ms | [![](./output/day6a.png)](./output/day6a.png) | Walk a long string for first occurrence of n unique characters where n=4
|6b|&nbsp; | 1ms | [![](./output/day6b.png)](./output/day6b.png)  | where n=14
|7a|No Space Left On Device [🌐](https://adventofcode.com/2022/day/7)[💾](./day7.py) | 0ms | [![](./output/day7a.png)](./output/day7a.png) | Track folder sizes in a Linux-like file system
|7b|&nbsp; | 0ms | [![](./output/day7b.png)](./output/day7b.png)  | Delete the right one to start the upgrade.  Will we see more of this Linux virtual computer later?
|8a|Treetop Tree House [🌐](https://adventofcode.com/2022/day/8)[💾](./day8.py) | 17ms | [![](./output/day8a.png)](./output/day8a.png) visible trees | find the local maximum from edges of a 2D array
|8b|&nbsp; | 59ms | [![](./output/day8b.png)](./output/day8b.png) tree house (white) | find the local maximums from each point in a 2D array - O(N2) alert!
|9a|Rope Bridge [🌐](https://adventofcode.com/2022/day/9)[💾](./day9.py) | 7ms | [![](./output/day9a.gif)](./output/day9a.gif) | overslept :( then massively overcomplicated the rope tail updater by using compound if-then-elses; replaced my original 2-knot head tail solution with generic version from part 2 with length 2
|9b|&nbsp; | 32ms | [![](./output/day9b.gif)](./output/day9b.gif)  | stuck for ages debugging complicated tail updater; eventually replaced that with much simpler version and it worked then simplified everything else to end up looking quite pleasing, good for animation too!
|10a|Cathode-Ray Tube [🌐](https://adventofcode.com/2022/day/10)[💾](./day10.py) | 0ms | [![](./output/day10a.png)](./output/day10a.png) | a comprehension test in two parts with asuitably satisfying end
|10b|&nbsp;| 0ms | [![](./output/day10b.png)](./output/day10b.png)  | hmm my code is all #s... a useful reminder that [["."]\*40]\*6 gives you 6 references to the same array!
|11a|[🌐](https://adventofcode.com/2022/day/11)[💾](./day11.py) | <!-- 0.0s --> | [![](./output/day11a.png)](./output/day11a.png) | 
|11b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day11b.png)](./output/day11b.png)  | 
|12a|[🌐](https://adventofcode.com/2022/day/12)[💾](./day12.py) | <!-- 0.0s --> | [![](./output/day12a.png)](./output/day12a.png) | 
|12b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day12b.png)](./output/day12b.png)  | 
|13a|[🌐](https://adventofcode.com/2022/day/13)[💾](./day13.py) | <!-- 0.0s --> | [![](./output/day13a.png)](./output/day13a.png) | 
|13b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day13b.png)](./output/day13b.png)  | 
|14a|[🌐](https://adventofcode.com/2022/day/14)[💾](./day14.py) | <!-- 0.0s --> | [![](./output/day14a.png)](./output/day14a.png) | 
|14b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day14b.png)](./output/day14b.png)  | 
|15a|[🌐](https://adventofcode.com/2022/day/15)[💾](./day15.py) | <!-- 0.0s --> | [![](./output/day15a.png)](./output/day15a.png) | 
|15b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day15b.png)](./output/day15b.png)  | 
|16a|[🌐](https://adventofcode.com/2022/day/16)[💾](./day16.py) | <!-- 0.0s --> | [![](./output/day16a.png)](./output/day16a.png) | 
|16b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day16b.png)](./output/day16b.png)  | 
|17a|[🌐](https://adventofcode.com/2022/day/17)[💾](./day17.py) | <!-- 0.0s --> | [![](./output/day17a.png)](./output/day17a.png) | 
|17b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day17b.png)](./output/day17b.png)  | 
|18a|[🌐](https://adventofcode.com/2022/day/18)[💾](./day18.py) | <!-- 0.0s --> | [![](./output/day18a.png)](./output/day18a.png) | 
|18b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day18b.png)](./output/day18b.png)  | 
|19a|[🌐](https://adventofcode.com/2022/day/19)[💾](./day19.py) | <!-- 0.0s --> | [![](./output/day19a.png)](./output/day19a.png) | 
|19b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day19b.png)](./output/day19b.png)  | 
|20a|[🌐](https://adventofcode.com/2022/day/20)[💾](./day20.py) | <!-- 0.0s --> | [![](./output/day20a.png)](./output/day20a.png) | 
|20b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day20b.png)](./output/day20b.png)  | 
|21a|[🌐](https://adventofcode.com/2022/day/21)[💾](./day21.py) | <!-- 0.0s --> | [![](./output/day21a.png)](./output/day21a.png) | 
|21b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day21b.png)](./output/day21b.png)  | 
|22a|[🌐](https://adventofcode.com/2022/day/22)[💾](./day22.py) | <!-- 0.0s --> | [![](./output/day22a.png)](./output/day22a.png) | 
|22b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day22b.png)](./output/day22b.png)  | 
|23a|[🌐](https://adventofcode.com/2022/day/23)[💾](./day23.py) | <!-- 0.0s --> | [![](./output/day23a.png)](./output/day23a.png) | 
|23b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day23b.png)](./output/day23b.png)  | 
|24a|[🌐](https://adventofcode.com/2022/day/24)[💾](./day24.py) | <!-- 0.0s --> | [![](./output/day24a.png)](./output/day24a.png) | 
|24b|&nbsp;                                                                                 | <!-- 0.0s --> | [![](./output/day24b.png)](./output/day24b.png)  | 
|25a|[🌐](https://adventofcode.com/2022/day/25)[💾](./day25.py) | <!-- 0.0s --> | [![](./output/day25a.png)](./output/day25a.png) | 

## Powershell

This year I am using a [powershell script](./input/download.ps1) to fetch my inputs, and open todays AoC22 puzzle triggered at 05:00:01 every morning (UK time) 🥱😴 or as soon as I log in 😊
