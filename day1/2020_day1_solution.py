
# coding: utf-8

# In[27]:


import csv


# In[28]:


with open('input1_.csv') as csvfile:
    readCSV = csv.reader(csvfile)
    list1 = []
    for row in readCSV:
        item = row[0]

        list1.append(item)


# In[29]:


#Part 1

for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        if i != j:
            if int(list1[i])+int(list1[j]) == 2020:
                print(list1[i], list1[j])
                print(int(list1[i])*int(list1[j]))
        
        


# In[26]:


#Part 2

for i in range(0, len(list1)):
    for j in range(0, len(list1)):
        for k in range(0, len(list1)):
            if i != j:
                if j != k:
                    if int(list1[i])+int(list1[j])+int(list1[k]) == 2020:
                        print(list1[i], list1[j], list1[k])
                        print(int(list1[i])*int(list1[j])*int(list1[k]))
        
        


# In[35]:


#Part 1 - better

from itertools import combinations

with open('input1_.csv') as csvfile:
    ls = [int(e.strip()) for e in csvfile.readlines()]
    
#Part 1
print ([e[0] * e[1] for e in combinations(ls, 2) if sum(e) == 2020][0])

#Part 2
print ([e[0] * e[1] * e[2] for e in combinations(ls, 3) if sum(e) == 2020][0])

