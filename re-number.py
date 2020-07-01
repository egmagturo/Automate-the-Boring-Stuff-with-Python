#!/usr/bin/env python
# coding: utf-8

# In[1]:


def isPhoneNumber(text): #415-555-0000
    if len(text) != 12:
        return False
    for i in range (0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range (4,7):
        if not text[i].isdecimal():
            return False
        if text[7] != '-':
            return False
    for i in range (8,12):
        if not text[i].isdecimal():
            return False
    return True

phone = input('Phone number: ')
isPhoneNumber(phone)
        

import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


# In[2]:


import re

phoneNumRegex = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
mo = phoneNumRegex.search('My number is 415-555-4242.')
print('Phone number found: ' + mo.group())


# In[ ]:




