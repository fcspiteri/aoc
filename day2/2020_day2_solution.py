
# coding: utf-8

# In[43]:


import csv

with open('input2.csv') as csvfile:
    ls = [str(l.strip()) for l in csvfile.readlines()]


# In[44]:


#Part 1 
pw_count = 0
for i in range(0, len(ls)):
    mn =  int((ls[i].split(' ')[0]).split('-')[0])
    mx =  int((ls[i].split(' ')[0]).split('-')[1])
    char = (ls[i].split(' ')[1]).split(':')[0]
    pw = ls[i].split(' ' )[2]
    
    count = 0
    for j in pw: 
        if j == char: 
            count = count + 1
    if count >= mn and count <= mx:
        pw_count = pw_count + 1
            
print (pw_count)


# In[45]:


#Part 2
pw_count = 0
for i in range(0, len(ls)):
    pos1 =  int((ls[i].split(' ')[0]).split('-')[0])-1
    pos2 =  int((ls[i].split(' ')[0]).split('-')[1])-1
    char = (ls[i].split(' ')[1]).split(':')[0]
    pw = ls[i].split(' ' )[2]
    
    if pw[pos1] == char and pw[pos2] != char:
        pw_count = pw_count + 1
    if pw[pos1] != char and pw[pos2] == char:
        pw_count = pw_count + 1
            
print (pw_count)

