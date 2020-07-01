#!/usr/bin/env python
# coding: utf-8

# In[36]:


#Take two lists, say for example these two:

 # a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
 # b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
#and write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes.

#Extras:

#Randomly generate two lists to test this
#Write this in one line of Python (don’t worry if you can’t figure this out at this point - we’ll get to it soon)

import random

randomlista = []
randomlistb = []
newlist = []

for i in range(11):
    n = random.randint(0,20)
    if n not in list:
        randomlista.append(n)
        
for j in range(11):
    m = random.randint(0,20)
    if m not in list:
        randomlistb.append(m)

print(randomlista)
print(randomlistb)

for k in randomlista:
    if k in randomlistb:
        newlist.append(k)

print(newlist)



# In[28]:


list = []
for i in range(1,11):
    n = random.randint(0,21)
    if n not in list:
        list.append(n)
print(list)


# In[ ]:





# In[ ]:




