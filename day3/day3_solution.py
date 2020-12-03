
# coding: utf-8

# In[1]:


import csv


# In[ ]:


'''
--- Day 3: Toboggan Trajectory ---
With the toboggan login problems resolved, you set off toward the airport. While travel by toboggan might be easy, it's certainly not safe: there's very minimal steering and the area is covered in trees. You'll need to see which angles will take you near the fewest trees.

Due to the local geology, trees in this area only grow on exact integer coordinates in a grid. You make a map (your puzzle input) of the open squares (.) and trees (#) you can see. For example:

..##.......
#...#...#..
.#....#..#.
..#.#...#.#
.#...##..#.
..#.##.....
.#.#.#....#
.#........#
#.##...#...
#...##....#
.#..#...#.#
These aren't the only trees, though; due to something you read about once involving arboreal genetics and biome stability, the same pattern repeats to the right many times:

..##.........##.........##.........##.........##.........##.......  --->
#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....#..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..#...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.##.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........#.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...##....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
You start on the open square (.) in the top-left corner and need to reach the bottom (below the bottom-most row on your map).

The toboggan can only follow a few specific slopes (you opted for a cheaper model that prefers rational numbers); start by counting all the trees you would encounter for the slope right 3, down 1:

From your starting position at the top-left, check the position that is right 3 and down 1. Then, check the position that is right 3 and down 1 from there, and so on until you go past the bottom of the map.

The locations you'd check in the above example are marked here with O where there was an open square and X where there was a tree:

..##.........##.........##.........##.........##.........##.......  --->
#..O#...#..#...#...#..#...#...#..#...#...#..#...#...#..#...#...#..
.#....X..#..#....#..#..#....#..#..#....#..#..#....#..#..#....#..#.
..#.#...#O#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#..#.#...#.#
.#...##..#..X...##..#..#...##..#..#...##..#..#...##..#..#...##..#.
..#.##.......#.X#.......#.##.......#.##.......#.##.......#.##.....  --->
.#.#.#....#.#.#.#.O..#.#.#.#....#.#.#.#....#.#.#.#....#.#.#.#....#
.#........#.#........X.#........#.#........#.#........#.#........#
#.##...#...#.##...#...#.X#...#...#.##...#...#.##...#...#.##...#...
#...##....##...##....##...#X....##...##....##...##....##...##....#
.#..#...#.#.#..#...#.#.#..#...X.#.#..#...#.#.#..#...#.#.#..#...#.#  --->
In this example, traversing the map using this slope would cause you to encounter 7 trees.

Starting at the top-left corner of your map and following a slope of right 3 and down 1, how many trees would you encounter?
'''


# In[72]:


#Part 1
with open('input3.csv') as csvfile:
    ls = [str(l.strip()) for l in csvfile.readlines()]
    
col = 0
trees = 0
mult = int(len(ls)/len(ls[0]))*4

for i in range(0, len(ls)):
    ls[i] = ls[i]*mult
rows = len(ls)
columns = len(ls[0])
for i in range(0, len(ls)):
    if ls[i][col] == "#":
        trees = trees + 1
    col = col + 3
    
print(trees)


# In[ ]:


'''
--- Part Two ---
Time to check the rest of the slopes - you need to minimize the probability of a sudden arboreal stop, after all.

Determine the number of trees you would encounter if, for each of the following slopes, you start at the top-left corner and traverse the map all the way to the bottom:

Right 1, down 1.
Right 3, down 1. (This is the slope you already checked.)
Right 5, down 1.
Right 7, down 1.
Right 1, down 2.
In the above example, these slopes would find 2, 7, 3, 4, and 2 tree(s) respectively; multiplied together, these produce the answer 336.

What do you get if you multiply together the number of trees encountered on each of the listed slopes?
'''


# In[83]:


#Part 2
with open('input3.csv') as csvfile:
    ls = [str(l.strip()) for l in csvfile.readlines()]
    
mult = int(len(ls)/len(ls[0]))*10

for i in range(0, len(ls)):
    ls[i] = ls[i]*mult
rows = len(ls)
columns = len(ls[0])

def trees(rise, run):
    col = 0
    trees = 0
    new_ls = ls[0::run]
    for i in range(0, len(new_ls)):
        if new_ls[i][col] == "#":
            trees = trees + 1
        col = col + rise
    return(trees)
print(trees(1, 1)*trees(3, 1)*trees(5, 1)*trees(7, 1)*trees(1, 2))


# In[8]:


''' Cleaner solution '''

#Open csv file into list
with open('input3.csv') as csvfile:
    ls = [str(l.strip()) for l in csvfile.readlines()]
    
def trees(rise, run):
    column = 0
    trees = 0
    new_ls = ls[0::rise] #Make new list that only includes rows in our slope
    for i in range(0, len(new_ls)):
        while column >= len(new_ls[i]):
            new_ls[i] = new_ls[i]+new_ls[i]
        if new_ls[i][column] == '#':
            trees = trees + 1
        column = column + run
    return (trees)

#Part 1
print('Part 1 solution: ',trees(1, 3))

#Part 2
print('Part 2 soltion: ', trees(1, 1)*trees(1, 3)*trees(1, 5)*trees(1, 7)*trees(2, 1))

