
# coding: utf-8

# In[1]:


import csv


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

