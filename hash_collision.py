#!/usr/bin/env python
# coding: utf-8

# In[1]:


import hashlib
import os
import string
import random


# In[2]:


M = ["Starbuck", "Stubb", "Flask"]   
L = [hashlib.sha256(x.encode('utf-8')).hexdigest() for x in M] 
print(L)


# In[3]:


#str = "Hello World"
#byte_str = str.encode('utf-8')
#print(byte_str)


# 1. Hash Collisions
# Use a brute-force algorithm to find a partial collision.
# Using the template “hash_collision.py” write a function called “hash_collision” that takes a single input, k, where k is an integer. The function “hash_collision” should return two variables, x and y, such that that the SHA256(x) and SHA256(y) match on their final k bits. The return variables, x and y, should be encoded as bytes.
# To encode a string as bytes
# str = "Hello World"
# byte_str = str.encode('utf-8')
# Your algorithm should be randomized, i.e., hash_collision(k) should not always return the same colliding pair.
# 
#     You need to get around 20 bits worth of collisions

# In[4]:


def get_key(val,mydict):
    for key, value in mydict.items():
        if val == value:
            return key
    return "key doesn't exist"


# In[5]:


def randomString(N):
    return ''.join(random.choice(string.ascii_lowercase + ' ') for i in range(N))
  


# In[9]:


def hash_collision(k):
    if not isinstance(k,int):
        print( "hash_collision expects an integer" )
        return( b'\x00',b'\x00' )
    if k <=0:
        print( "Specify a positive number of bits" )
        return( b'\x00',b'\x00' )
   
    #Collision finding code goes here
    totalBits = 256
    collisionBits = k
    count = 0 
    n=100
    mydict = {}

        
        
    while True:
        msgX = randomString(n)
        msgY = randomString(n)
        digX = hashlib.sha256(msgX.encode(encoding='utf_8', errors='strict')).hexdigest()
        digY = hashlib.sha256(msgY.encode(encoding='utf_8', errors='strict')).hexdigest()
    
        valueX = digX[-k:]
        valueY = digY[-k:]
        keyX = msgX
        keyY = msgY
    
        if valueY in mydict.values():
            y = msgY.encode('utf-8')
            x = get_key(valueY,mydict).encode('utf-8')
            return( x, y )
        
        if valueX not in mydict.values():
            mydict.update({keyX:valueX})
    
        if valueY not in mydict.values():
            mydict.update({keyY:valueY})
    
    
    x = b'\x00'
    y = b'\x00'
    
    return( x, y )


